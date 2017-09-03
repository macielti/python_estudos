import admin

bruno= admin.Admin('bruno', 'do nascimentom maciel', '18', 'brasil')

bruno.privileges= admin.Privileges('dinheiro inifinito', 'adicionar user',
                                    'voar', 'atravessar paredes')

bruno.privileges.show_privileges()
