#!/bin/bash
cat 00.md > README.md

for (( i = 1; i <= 2; i++ )); do
    id=`printf "%02d" ${i}`
    cat ${id}.md >> README.md
    echo \`\`\`c >> README.md
    cat ${id}.c >> README.md
    echo >> README.md
    echo \`\`\` >> README.md
done

echo >> README.md
echo >> README.md
echo >> README.md
echo >> README.md

