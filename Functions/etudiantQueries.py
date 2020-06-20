from Functions.Connection_DB import execute_query


def get_etudiant_info(num_etudiant):
    return execute_query("select * from etudiant where num = " + "'" + num_etudiant + "'", False)


def is_etudiant_exist(num_etudiant):
    return len(get_etudiant_info(num_etudiant)) != 0


def get_etudiants_info():
    return execute_query("select * from etudiant", False)


def is_etudiants_exist():
    return len(get_etudiants_info()) != 0


def add_etudiant(num, prenom, nom, niveau):
    res = execute_query("insert into etudiant values ('" + num + "','" + prenom + "','" + nom + "','" + niveau + "')",
                        True)

    if len(res) == 0:
        print('Une erreur est survenue')
    else:
        print(etudiant_to_string(num, prenom, nom, niveau) + ' est sauvegarde avec succes')


def update_etudiant(num, prenom='', nom='', niveau=''):
    query = ''

    # etudiant exist
    if is_etudiant_exist(num):
        # prenom seul
        if prenom and nom == '' and niveau == '':
            query = 'update etudiant set prenom = \'' + prenom + '\' where (num = \'' + num + '\')'
        # prenom et nom seul
        elif prenom and nom and niveau == '':
            query = 'update etudiant set prenom = \'' + prenom + '\', nom = \'' + nom + '\' where (num = \'' + num + '\')'

        # nom seul
        elif prenom == '' and nom and niveau == '':
            query = 'update etudiant set prenom = \'' + prenom + '\' where (num = \'' + num + '\')'
        # nom et niveau seul
        elif prenom == '' and nom and niveau:
            query = 'update etudiant set prenom = \'' + prenom + '\', nom = \'' + nom + '\' where (num = \'' + num + '\')'

        # niveau seul
        elif prenom == '' and nom == '' and niveau:
            query = 'update etudiant set prenom = \'' + prenom + '\' where (num = \'' + num + '\')'
        # niveau et prenom seul
        elif prenom and nom == '' and niveau:
            query = 'update etudiant set prenom = \'' + prenom + '\', nom = \'' + nom + '\' where (num = \'' + num + '\')'
        # toutes est remplis
        elif prenom and nom and niveau:
            query = 'update etudiant set prenom = \'' + prenom + '\', nom = \'' + nom + '\',niveau = \'' + niveau + \
                    '\' where (num = \'' + num + '\') '

        res = execute_query(query, True)

        if len(res) == 0:
            print('Une erreur est survenue')
        else:
            print(etudiant_to_string(num, prenom, nom, niveau) + ' est modifie avec succes')

    # etudiant n'existe pas
    else:
        print('Etudiant \'' + num + '\' n\'existe pas')


def delete_etudiant(num):
    # etudiant exist
    if is_etudiant_exist(num):
        detailed_info = get_detailed_etudiant_info(num)[0]

        res = execute_query("delete from etudiant where num = " + "'" + num + "'", True)

        if len(res) == 0:
            print('Une erreur est survenue')
        else:
            # get prenom, nom et niveau de l'etudiant
            print(etudiant_to_string(num, detailed_info['prenom'], detailed_info['nom'],
                                     detailed_info['niveau']) + ' est supprime avec succes')

    # etudiant n'existe pas
    else:
        print('Etudiant \'' + num + '\' n\'existe pas')


def get_detailed_etudiant_info(num=''):
    all_etudiant_info = []

    if num == '':
        res = get_etudiants_info()
    else:
        res = get_etudiant_info(num)

    if len(res) != 0:
        for each_etudiant in res:
            all_etudiant_info.append(
                {
                    'num': each_etudiant[0],
                    'prenom': each_etudiant[1],
                    'nom': each_etudiant[2],
                    'niveau': each_etudiant[3]
                }
            )

    return all_etudiant_info


def etudiant_to_string(num, prenom, nom, niveau):
    return 'L\'etudiant qui a pour info \'' + str(prenom.capitalize()) + ' ' + str(
        nom.capitalize()) + ' Niveau ' + niveau + ' ' + '(' + num + ')' + '\''
