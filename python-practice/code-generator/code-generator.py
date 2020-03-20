# coding:utf-8

"""
--templates-path templates # 需要生成的文件模版（可能是多模板）目录
--class-name Access # 生成文件中类名
--type-map # 数据库字段类型与生成代码类型的转换关系表

python3 code-generator.py \
--templates-path templates \
--type-map type-map.ini \
--table-prefix jjrxt_ \
--table-name access \
--class-name Access

"""
import os
import sys
import argparse
import json
import pymysql


def get_conn(__db_info__):
    return pymysql.connect(
        host=__db_info__['host'],
        port=__db_info__['port'],
        user=__db_info__['user'],
        password=__db_info__['pass'],
        database='information_schema',
        charset='utf8'
    )


def mysql_get_first(__db_info__, __sql__):
    conn = get_conn(__db_info__)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(__sql__)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def mysql_get_list(__db_info__, __sql__):
    conn = get_conn(__db_info__)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(__sql__)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def load_db_info(__db_info_path__):
    obj = json.load(open(__db_info_path__, 'r'))
    keys = ['host', 'port', 'user', 'pass', 'name']
    for key in keys:
        if key not in obj:
            print('db.json invalid')
            exit(-1)
    return obj


def load_type_map(__type_map_file__):
    try:
        with open(__type_map_file__, 'r') as f:
            type_map = {}
            for line in f.readlines():
                line = line.strip()
                if not line[0] == '#' and '=' in line:
                    type_map[line[:line.find('=')]] = line[line.find('=') + 1:]
            return type_map
    except:
        exit(0)
        return {}


def is_template_file(__file_path__):
    try:
        with open(__file_path__, 'r') as f:
            content = f.readlines()
            if len(content) >= 2 and content[1][:3] == '---':
                return True
        return False
    except:
        return False


def extract_template_file(__file_path__):
    if not is_template_file(__file_path__):
        return None, None
    with open(__file_path__, 'r') as f:
        lines = f.readlines()
        path = lines[0].strip()
        content = ''
        for line in lines[2:]:
            content += line
        return path, content


def fetch_template_list(__templates_path__):
    files = os.listdir(__templates_path__)
    template_list = []
    for file in files:
        template_file_path = __templates_path__ + '/' + file
        if os.path.isfile(template_file_path) and is_template_file(template_file_path):
            template_list.append(template_file_path)
    return template_list


def parse_list_section(__section__, __template_path__, __data__):
    section_tpl = __section__[__section__.find(':') + 1: __section__.find('}')]
    section_content = ''
    content = ''
    with open(__template_path__ + '/sections/' + section_tpl, 'r') as f:
        section_content = f.read()
    for table_column in __data__['table_columns']:
        tmp_content = section_content
        tmp_content = tmp_content.replace('${column_type}', '%-9s' % __data__['type_map'][table_column['DATA_TYPE']])
        tmp_content = tmp_content.replace('${column_name}', '%-15s' % table_column['COLUMN_NAME'])
        tmp_content = tmp_content.replace('${column_comment}', table_column['COLUMN_COMMENT'])
        content += tmp_content
    return content


def parse_template(__content__, __template_path__, __data__):
    __content__ = __content__.replace('${class_name}', __data__['class_name'])
    __content__ = __content__.replace('${table_name}', __data__['table_name'])
    __content__ = __content__.replace('{$table_comment}', __data__['table_info']['TABLE_COMMENT'])
    while "${list:" in __content__:
        list_section = __content__[__content__.find('${list:'):]
        list_section = list_section[:list_section.find('}') + 1]
        list_section_content = parse_list_section(list_section, __template_path__, __data__)
        __content__ = __content__.replace(list_section, list_section_content)
    return __content__


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db-info', default='db.json', help='MySQL Database Connection Info')
    parser.add_argument('--templates-path', required=True, help='Templates Path')
    parser.add_argument('--type-map', required=True, help='Type Map File for Mapping mysql type to code type, '
                                                          'e.g. varchar=string')
    parser.add_argument('--table-prefix', default='', help='Table name prefix')
    parser.add_argument('--table-name', required=True, help='Table Name')
    parser.add_argument('--class-name', required=True, help='Class Name')
    args = parser.parse_args()
    db_info = load_db_info(args.db_info)
    templates_path = args.templates_path
    type_map = args.type_map
    table_prefix = args.table_prefix
    table_name = args.table_name
    class_name = args.class_name
    # Load type map
    type_map = load_type_map(type_map)
    # read table info from database
    table_info = mysql_get_first(db_info, "select * from TABLES where TABLE_SCHEMA='%s' and TABLE_NAME='%s%s';" % (
        db_info['name'], table_prefix, table_name))
    if table_info is None:
        print('table [%s%s] is not exists.' % (table_prefix, table_name))
        exit(-1)
    # read table columns from database
    table_columns = mysql_get_list(db_info,
                                   "select * from COLUMNS where TABLE_SCHEMA='%s' and TABLE_NAME='%s%s' order by ORDINAL_POSITION asc;" % (
                                       db_info['name'], table_prefix, table_name))
    # Data
    data = {
        'class_name': class_name,
        'table_info': table_info,
        'table_prefix': table_prefix,
        'table_name': table_name,
        'table_columns': table_columns,
        'type_map': type_map
    }
    # Fetch template list
    template_list = fetch_template_list(templates_path)
    for template_file in template_list:
        path, content = extract_template_file(template_file)
        path = parse_template(path, templates_path, data)
        content = parse_template(content, templates_path, data)
        with open(path, 'a') as f:
            f.write(content)
        print(path)


if __name__ == '__main__':
    main()
