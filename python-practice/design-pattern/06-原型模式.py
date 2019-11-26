# coding:utf-8


class EventTemplate(object):
    event_subject = ''
    event_content = ''

    def __init__(self, event_subject, event_content):
        self.event_subject = event_subject
        self.event_content = event_content


class Mail(object):
    receiver = ''
    subject = ''
    content = ''
    tail = ''

    def __init__(self, event_template: EventTemplate):
        self.tail = event_template.event_content
        self.subject = event_template.event_subject


def send_mail(mail: Mail):
    mail.content = '%s,先生（女士）：你的信用卡账单...' % mail.receiver
    print(mail.receiver)
    print(mail.subject)
    print(mail.content)


def main():
    et = EventTemplate("9月份信用卡账单", "国庆抽奖活动...")
    mail = Mail(et)
    mail.receiver = 'Del Cooper'
    send_mail(mail)


if __name__ == '__main__':
    main()
