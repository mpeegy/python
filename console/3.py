#!/usr/bin/env python
import optparse
from subprocess import Popen, PIPE
import re
def main():
    p = optparse.OptionParser(description="Python wrapped snmpdf command",
                              prog="pysnmpdf",
                              version="0.1a",
                              usage="%prog machine")
    p.add_option("�c", "��community", help="snmp community string")
    p.add_option("�V", "��Version", help="snmp version to use")
    p.set_defaults(community="public",Version="2c")
    options, arguments = p.parse_args()
    SNMPDF = "snmpdf"
    if len(arguments) == 1:
        machine = arguments[0]
  #Вложенная функция�генератор
        def parse():
            """Возвращает объект�генератор со строкой от команды snmpdf"""
            ps = Popen([SNMPDF, "�c", options.community,
                        "�v",options.Version, machine],
                        stdout=PIPE, stderr=PIPE)
            return ps.stdout
        #Конвейер генераторов для поиска критических значений
        pattern = "9[0�9]%"
        outline = (line.split() for line in parse()) #удалить возвраты каретки
        flag = (" ".join(row) for row in outline if re.search(pattern, 
                                                              row[�1]))
        #поиск по шаблону и объединение соответствующих строк в список
        for line in flag: print "%s CRITICAL" % line
        #Пример возвращаемого значения
        #Real Memory 2067636 1974120 93516 95% CRITICAL
    else:
        p.print_help()
if __name__ == '__main__':
    main()
