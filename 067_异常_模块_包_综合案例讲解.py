from related_data.my_utils import str_util
from related_data.my_utils import file_util

str_util.str_reverse('Iven enjoys coding')
str_util.substr('Iven enjoys coding', 3 , 9)

file_util.print_file_info('related_data/package.txt')
file_util.append_to_file('related_data/package.txt', 'Iven')