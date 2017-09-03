import privileges_and_admin

bruno= privileges_and_admin.Admin('bruno', 'do nascimento maciel', 18, 'brasil')

bruno.privileges= privileges_and_admin.Privileges('voar', 'adicionar users',
                                                    'modificar atributos')
                                                    
bruno.privileges.show_privileges()
