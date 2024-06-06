### APPARATUS FOR FILTERING DUPLICATES FROM KINSHIP SYSTEMS ###

age_split = [['mM','mM','mM'], ['mF','mF','mF'], 
             ['mMB','mMeB','mMyB'], ['mFB','mFeB','mFyB'], ['mMZ','mMeZ','mMyZ'], ['mFZ','mFeZ','mFyZ'],
             ['mB','meB','myB'],['mZ','meZ','myZ'],
             ['mMBS','mMBeS','mMByS'],['mMeBS','mMeBeS','mMeByS'],['mMyBS','mMyBeS','mMyByS'],
             ['mFBS','mFBeS','mFByS'],['mFeBS','mFeBeS','mFeByS'],['mFyBS','mFyBeS','mFyByS'],
             ['mMZS','mMZeS','mMZyS'],['mMeZS','mMeZeS','mMeZyS'],['mMyZS','mMyZeS','mMyZyS'],
             ['mFZS','mFZeS','mFZyS'],['mFeZS','mFeZeS','mFeZyS'],['mFyZS','mFyZeS','mFyZyS'],
             ['mMBD','mMBeD','mMByD'],['mMeBD','mMeBeD','mMeByD'],['mMyBD','mMyBeD','mMyByD'],
             ['mFBD','mFBeD','mFByD'],['mFeBD','mFeBeD','mFeByD'],['mFyBD','mFyBeD','mFyByD'],
             ['mMZD','mMZeD','mMZyD'],['mMeZD','mMeZeD','mMeZyD'],['mMyZD','mMyZeD','mMyZyD'],
             ['mFZD','mFZeD','mFZyD'],['mFeZD','mFeZeD','mFeZyD'],['mFyZD','mFyZeD','mFyZyD'],
             ['mMBS','mMeBS','mMyBS'],['mMBD','mMeBD','mMyBD'],['mMZS','mMeZS','mMyZS'],['mMZD','mMeZD','mMyZD'],
             ['mFBS','mFeBS','mFyBS'],['mFBD','mFeBD','mFyBD'],['mFZS','mFeZS','mFyZS'],['mFZD','mFeZD','mFyZD'],
             
             ['fM','fM','fM'], ['fF','fF','fF'],
             ['fMB','fMeB','fMyB'],['fFB','fFeB','fFyB'],['fMZ','fMeZ','fMyZ'],['fFZ','fFeZ','fFyZ'],
             ['fB','feB','fyB'],['fZ','feZ','fyZ'],
             ['fMBS','fMBeS','fMByS'],['fMeBS','fMeBeS','fMeByS'],['fMyBS','fMyBeS','fMyByS'],
             ['fFBS','fFBeS','fFByS'],['fFeBS','fFeBeS','fFeByS'],['fFyBS','fFyBeS','fFyByS'],
             ['fMZS','fMZeS','fMZyS'],['fMeZS','fMeZeS','fMeZyS'],['fMyZS','fMyZeS','fMyZyS'],
             ['fFZS','fFZeS','fFZyS'],['fFeZS','fFeZeS','fFeZyS'],['fFyZS','fFyZeS','fFyZyS'],
             ['fMBD','fMBeD','fMByD'],['fMeBD','fMeBeD','fMeByD'],['fMyBD','fMyBeD','fMyByD'],
             ['fFBD','fFBeD','fFByD'],['fFeBD','fFeBeD','fFeByD'],['fFyBD','fFyBeD','fFyByD'],
             ['fMZD','fMZeD','fMZyD'],['fMeZD','fMeZeD','fMeZyD'],['fMyZD','fMyZeD','fMyZyD'],
             ['fFZD','fFZeD','fFZyD'],['fFeZD','fFeZeD','fFeZyD'],['fFyZD','fFyZeD','fFyZyD'],
             ['fMBS','fMeBS','fMyBS'],['fMBD','fMeBD','fMyBD'],['fMZS','fMeZS','fMyZS'],['fMZD','fMeZD','fMyZD'],
             ['fFBS','fFeBS','fFyBS'],['fFBD','fFeBD','fFyBD'],['fFZS','fFeZS','fFyZS'],['fFZD','fFeZD','fFyZD']]

             


# parents and siblings, male speaker
Mpar_sib = {
    "mother": ['mM','mM','mM'],
    "father": ['mF','mF','mF'],
    "mother's brother": ['mMB','mMeB','mMyB'],
    "father's brother": ['mFB','mFeB','mFyB'],
    "mother's sister": ['mMZ','mMeZ','mMyZ'],
    "father's sister": ['mFZ','mFeZ','mFyZ'],
    'brother': ['mB','meB','myB'],
    'sister': ['mZ','meZ','myZ'],
}

# male cousins, male speaker
cousMS = {
    'mMB': ['mMBS','mMBeS','mMByS'],
    'mMeB': ['mMeBS','mMeBeS','mMeByS'],
    'mMyB': ['mMyBS','mMyBeS','mMyByS'],
    'mFB': ['mFBS','mFBeS','mFByS'],
    'mFeB': ['mFeBS','mFeBeS','mFeByS'],
    'mFyB': ['mFyBS','mFyBeS','mFyByS'],
    'mMZ': ['mMZS','mMZeS','mMZyS'],
    'mMeZ': ['mMeZS','mMeZeS','mMeZyS'],
    'mMyZ': ['mMyZS','mMyZeS','mMyZyS'],
    'mFZ': ['mFZS','mFZeS','mFZyS'],
    'mFeZ': ['mFeZS','mFeZeS','mFeZyS'],
    'mFyZ': ['mFyZS','mFyZeS','mFyZyS'],
}

# female cousins male speaker
cousMD = {
    'mMB': ['mMBD','mMBeD','mMByD'],
    'mMeB': ['mMeBD','mMeBeD','mMeByD'],
    'mMyB': ['mMyBD','mMyBeD','mMyByD'],
    'mFB': ['mFBD','mFBeD','mFByD'],
    'mFeB': ['mFeBD','mFeBeD','mFeByD'],
    'mFyB': ['mFyBD','mFyBeD','mFyByD'],
    'mMZ': ['mMZD','mMZeD','mMZyD'],
    'mMeZ': ['mMeZD','mMeZeD','mMeZyD'],
    'mMyZ': ['mMyZD','mMyZeD','mMyZyD'],
    'mFZ': ['mFZD','mFZeD','mFZyD'],
    'mFeZ': ['mFeZD','mFeZeD','mFeZyD'],
    'mFyZ': ['mFyZD','mFyZeD','mFyZyD'],
}

# parents and siblings female speaker
Fpar_sib = {
    "mother": ['fM','fM','fM'],
    "father": ['fF','fF','fF'],
    "mother's brother": ['fMB','fMeB','fMyB'],
    "father's brother": ['fFB','fFeB','fFyB'],
    "mother's sister": ['fMZ','fMeZ','fMyZ'],
    "father's sister": ['fFZ','fFeZ','fFyZ'],
    'brother': ['fB','feB','fyB'],
    'sister': ['fZ','feZ','fyZ'],
}

# male cousins female speaker
cousFS = {
    'fMB': ['fMBS','fMBeS','fMByS'],
    'fMeB': ['fMeBS','fMeBeS','fMeByS'],
    'fMyB': ['fMyBS','fMyBeS','fMyByS'],
    'fFB': ['fFBS','fFBeS','fFByS'],
    'fFeB': ['fFeBS','fFeBeS','fFeByS'],
    'fFyB': ['fFyBS','fFyBeS','fFyByS'],
    'fMZ': ['fMZS','fMZeS','fMZyS'],
    'fMeZ': ['fMeZS','fMeZeS','fMeZyS'],
    'fMyZ': ['fMyZS','fMyZeS','fMyZyS'],
    'fFZ': ['fFZS','fFZeS','fFZyS'],
    'fFeZ': ['fFeZS','fFeZeS','fFeZyS'],
    'fFyZ': ['fFyZS','fFyZeS','fFyZyS'],
}

# female cousins female speaker
cousFD = {
    'fMB': ['fMBD','fMBeD','fMByD'],
    'fMeB': ['fMeBD','fMeBeD','fMeByD'],
    'fMyB': ['fMyBD','fMyBeD','fMyByD'],
    'fFB': ['fFBD','fFBeD','fFByD'],
    'fFeB': ['fFeBD','fFeBeD','fFeByD'],
    'fFyB': ['fFyBD','fFyBeD','fFyByD'],
    'fMZ': ['fMZD','fMZeD','fMZyD'],
    'fMeZ': ['fMeZD','fMeZeD','fMeZyD'],
    'fMyZ': ['fMyZD','fMyZeD','fMyZyD'],
    'fFZ': ['fFZD','fFZeD','fFZyD'],
    'fFeZ': ['fFeZD','fFeZeD','fFeZyD'],
    'fFyZ': ['fFyZD','fFyZeD','fFyZyD'],
}

m_speaker = ['mB','mZ',
             'meB', 'meZ',
             'myB', 'myZ',
             'mMeZeS','mMeZeD', 'mMeZyS', 'mMeZyD','mMeZS', 'mMeZD',
             'mMeBeS', 'mMeBeD', 'mMeByS', 'mMeByD', 'mMeBS','mMeBD',
             'mMyZeS', 'mMyZeD', 'mMyZyS', 'mMyZyD', 'mMyZS', 'mMyZD',
             'mMyBeS', 'mMyBeD', 'mMyByS', 'mMyByD', 'mMyBS', 'mMyBD',
             'mFeZeS','mFeZeD', 'mFeZyS', 'mFeZyD','mFeZS', 'mFeZD',
             'mFeBeS', 'mFeBeD','mFeByS', 'mFeByD', 'mFeBS', 'mFeBD',
             'mFyZeS', 'mFyZeD', 'mFyZyS','mFyZyD', 'mFyZS', 'mFyZD',
             'mFyBeS', 'mFyBeD', 'mFyByS', 'mFyByD','mFyBS', 'mFyBD',
             'mMZeS','mMZeD','mMZyS','mMZyD','mMZS','mMZD',
             'mMBeS','mMBeD','mMByS','mMByD','mMBS','mMBD',
             'mFZeS','mFZeD','mFZyS','mFZyD','mFZS','mFZD',
             'mFBeS','mFBeD','mFByS','mFByD','mFBS','mFBD',
             'mMB','mMZ',
             'mFB','mFZ',
             'mM','mF',
             'mMeB','mMeZ',
             'mMyB','mMyZ',
             'mFeB','mFeZ',
             'mFyB','mFyZ']
 
f_speaker = ['fB','fZ',
             'feB', 'feZ',
             'fyB', 'fyZ',
                'fMeZeS','fMeZeD', 'fMeZyS', 'fMeZyD','fMeZS', 'fMeZD',
                'fMeBeS', 'fMeBeD', 'fMeByS', 'fMeByD', 'fMeBS','fMeBD',
                'fMyZeS', 'fMyZeD', 'fMyZyS', 'fMyZyD', 'fMyZS', 'fMyZD',
                'fMyBeS', 'fMyBeD', 'fMyByS', 'fMyByD', 'fMyBS', 'fMyBD',
                'fFeZeS','fFeZeD', 'fFeZyS', 'fFeZyD','fFeZS', 'fFeZD',
                'fFeBeS', 'fFeBeD','fFeByS', 'fFeByD', 'fFeBS', 'fFeBD',
                'fFyZeS', 'fFyZeD', 'fFyZyS','fFyZyD', 'fFyZS', 'fFyZD',
                'fFyBeS', 'fFyBeD', 'fFyByS', 'fFyByD','fFyBS', 'fFyBD',
                'fMZeS','fMZeD','fMZyS','fMZyD','fMZS','fMZD',
                'fMBeS','fMBeD','fMByS','fMByD','fMBS','fMBD',
                'fFZeS','fFZeD','fFZyS','fFZyD','fFZS','fFZD',
                'fFBeS','fFBeD','fFByS','fFByD','fFBS','fFBD',
                 'fMB','fMZ',
                 'fFB','fFZ',
                 'fM','fF',
                 'fMeB','fMeZ',
                 'fMyB','fMyZ',
                 'fFeB','fFeZ',
                 'fFyB','fFyZ']

### KIN TYPES IN EACH GENERATION ###

generation_n = [#'mB','mZ',
                'meB', 'meZ',
                'myB', 'myZ',
                'mMeZeS','mMeZeD', 'mMeZyS', 'mMeZyD','mMeZS', 'mMeZD',
                'mMeBeS', 'mMeBeD', 'mMeByS', 'mMeByD', 'mMeBS','mMeBD',
                'mMyZeS', 'mMyZeD', 'mMyZyS', 'mMyZyD', 'mMyZS', 'mMyZD',
                'mMyBeS', 'mMyBeD', 'mMyByS', 'mMyByD', 'mMyBS', 'mMyBD',
                'mFeZeS','mFeZeD', 'mFeZyS', 'mFeZyD','mFeZS', 'mFeZD',
                'mFeBeS', 'mFeBeD','mFeByS', 'mFeByD', 'mFeBS', 'mFeBD',
                'mFyZeS', 'mFyZeD', 'mFyZyS','mFyZyD', 'mFyZS', 'mFyZD',
                'mFyBeS', 'mFyBeD', 'mFyByS', 'mFyByD','mFyBS', 'mFyBD',
                #'mMZeS','mMZeD','mMZyS','mMZyD','mMZS','mMZD',
                #'mMBeS','mMBeD','mMByS','mMByD','mMBS','mMBD',
                #'mFZeS','mFZeD','mFZyS','mFZyD','mFZS','mFZD',
                #'mFBeS','mFBeD','mFByS','mFByD','mFBS','mFBD',
                #'fB','fZ',
                'feB', 'feZ',
                'fyB', 'fyZ',
                'fMeZeS','fMeZeD', 'fMeZyS', 'fMeZyD','fMeZS', 'fMeZD',
                'fMeBeS', 'fMeBeD', 'fMeByS', 'fMeByD', 'fMeBS','fMeBD',
                'fMyZeS', 'fMyZeD', 'fMyZyS', 'fMyZyD', 'fMyZS', 'fMyZD',
                'fMyBeS', 'fMyBeD', 'fMyByS', 'fMyByD', 'fMyBS', 'fMyBD',
                'fFeZeS','fFeZeD', 'fFeZyS', 'fFeZyD','fFeZS', 'fFeZD',
                'fFeBeS', 'fFeBeD','fFeByS', 'fFeByD', 'fFeBS', 'fFeBD',
                'fFyZeS', 'fFyZeD', 'fFyZyS','fFyZyD', 'fFyZS', 'fFyZD',
                'fFyBeS', 'fFyBeD', 'fFyByS', 'fFyByD','fFyBS', 'fFyBD']
                #'fMZeS','fMZeD','fMZyS','fMZyD','fMZS','fMZD',
                #'fMBeS','fMBeD','fMByS','fMByD','fMBS','fMBD',
                #'fFZeS','fFZeD','fFZyS','fFZyD','fFZS','fFZD',
                #'fFBeS','fFBeD','fFByS','fFByD','fFBS','fFBD']


generation_n1 = [#'mMB','mMZ',
                 #'mFB','mFZ',
                 'mM','mF',
                 'mMeB','mMeZ',
                 'mMyB','mMyZ',
                 'mFeB','mFeZ',
                 'mFyB','mFyZ',
                 #'fMB','fMZ',
                 #'fFB','fFZ',
                 'fM','fF',
                 'fMeB','fMeZ',
                 'fMyB','fMyZ',
                 'fFeB','fFeZ',
                 'fFyB','fFyZ']


### GENDER DISTINGUISHED PAIRS ###

ge_pairs = [('mB','mZ'),('meB','meZ'),('myB','myZ'),
         ('mMeZeS','mMeZeD'),('mMeZyS','mMeZyD'),('mMeZS','mMeZD'),
         ('mMyZeS','mMyZeD'),('mMyZyS','mMyZyD'),('mMyZS','mMyZD'),
         ('mMZeS','mMZeD'),('mMZyS','mMZyD'),('mMZS','mMZD'),
         ('mMeBeS','mMeBeD'),('mMeByS','mMeByD'),('mMeBS','mMeBD'),
         ('mMyBeS','mMyBeD'),('mMyByS','mMyByD'),('mMyBS','mMyBD'),
         ('mMBeS','mMBeD'),('mMByS','mMByD'),('mMBS','mMBD'),
         ('mFeZeS','mFeZeD'),('mFeZyS','mFeZyD'),('mFeZS','mFeZD'),
         ('mFyZeS','mFyZeD'),('mFyZyS','mFyZyD'),('mFyZS','mFyZD'),
         ('mFZeS','mFZeD'),('mFZyS','mFZyD'),('mFZS','mFZD'),
         ('mFeBeS','mFeBeD'),('mFeByS','mFeByD'),('mFeBS','mFeBD'),
         ('mFyBeS','mFyBeD'),('mFyByS','mFyByD'),('mFyBS','mFyBD'),
         ('mFBeS','mFBeD'),('mFByS','mFByD'),('mFBS','mFBD'),
         ('mMB','mMZ'),('mFB','mFZ'),
         ('mMeB','mMeZ'),('mMyB','mMyZ'),
         ('mFeB','mFeZ'),('mFyB','mFyZ'),
         ('fB','fZ'),('feB','feZ'),('fyB','fyZ'),
         ('fMeZeS','fMeZeD'),('fMeZyS','fMeZyD'),('fMeZS','fMeZD'),
         ('fMyZeS','fMyZeD'),('fMyZyS','fMyZyD'),('fMyZS','fMyZD'),
         ('fMZeS','fMZeD'),('fMZyS','fMZyD'),('fMZS','fMZD'),
         ('fMeBeS','fMeBeD'),('fMeByS','fMeByD'),('fMeBS','fMeBD'),
         ('fMyBeS','fMyBeD'),('fMyByS','fMyByD'),('fMyBS','fMyBD'),
         ('fMBeS','fMBeD'),('fMByS','fMByD'),('fMBS','fMBD'),
         ('fFeZeS','fFeZeD'),('fFeZyS','fFeZyD'),('fFeZS','fFeZD'),
         ('fFyZeS','fFyZeD'),('fFyZyS','fFyZyD'),('fFyZS','fFyZD'),
         ('fFZeS','fFZeD'),('fFZyS','fFZyD'),('fFZS','fFZD'),
         ('fFeBeS','fFeBeD'),('fFeByS','fFeByD'),('fFeBS','fFeBD'),
         ('fFyBeS','fFyBeD'),('fFyByS','fFyByD'),('fFyBS','fFyBD'),
         ('fFBeS','fFBeD'),('fFByS','fFByD'),('fFBS','fFBD'),
         ('fMB','fMZ'),('fFB','fFZ'),
         ('fMeB','fMeZ'),('fMyB','fMyZ'),
         ('fFeB','fFeZ'),('fFyB','fFyZ')]

ge_gN = [('mB','mZ'),('meB','meZ'),('myB','myZ'),('mMeZeS','mMeZeD'),('mMeZyS','mMeZyD'),('mMeZS','mMeZD'),
('mMyZeS','mMyZeD'),('mMyZyS','mMyZyD'),('mMyZS','mMyZD'),('mMZeS','mMZeD'),('mMZyS','mMZyD'),('mMZS','mMZD'),
('mMeBeS','mMeBeD'),('mMeByS','mMeByD'),('mMeBS','mMeBD'),('mMyBeS','mMyBeD'),('mMyByS','mMyByD'),('mMyBS','mMyBD'),
('mMBeS','mMBeD'),('mMByS','mMByD'),('mMBS','mMBD'),('mFeZeS','mFeZeD'),('mFeZyS','mFeZyD'),('mFeZS','mFeZD'),
('mFyZeS','mFyZeD'),('mFyZyS','mFyZyD'),('mFyZS','mFyZD'),('mFZeS','mFZeD'),('mFZyS','mFZyD'),('mFZS','mFZD'),
('mFeBeS','mFeBeD'),('mFeByS','mFeByD'),('mFeBS','mFeBD'),('mFyBeS','mFyBeD'),('mFyByS','mFyByD'),('mFyBS','mFyBD'),
('mFBeS','mFBeD'),('mFByS','mFByD'),('mFBS','mFBD'),('fB','fZ'),('feB','feZ'),('fyB','fyZ'),('fMeZeS','fMeZeD'),('fMeZyS','fMeZyD'),('fMeZS','fMeZD'),('fMyZeS','fMyZeD'),('fMyZyS','fMyZyD'),('fMyZS','fMyZD'),('fMZeS','fMZeD'),('fMZyS','fMZyD'),('fMZS','fMZD'),
('fMeBeS','fMeBeD'),('fMeByS','fMeByD'),('fMeBS','fMeBD'),('fMyBeS','fMyBeD'),('fMyByS','fMyByD'),('fMyBS','fMyBD'),
('fMBeS','fMBeD'),('fMByS','fMByD'),('fMBS','fMBD'),('fFeZeS','fFeZeD'),('fFeZyS','fFeZyD'),('fFeZS','fFeZD'),
('fFyZeS','fFyZeD'),('fFyZyS','fFyZyD'),('fFyZS','fFyZD'),('fFZeS','fFZeD'),('fFZyS','fFZyD'),('fFZS','fFZD'),
('fFeBeS','fFeBeD'),('fFeByS','fFeByD'),('fFeBS','fFeBD'),('fFyBeS','fFyBeD'),('fFyByS','fFyByD'),('fFyBS','fFyBD'),
('fFBeS','fFBeD'),('fFByS','fFByD'),('fFBS','fFBD')]

ge_gN1 = [('mMB','mMZ'),('mFB','mFZ'),('mMeB','mMeZ'),('mMyB','mMyZ'),('mFeB','mFeZ'),('mFyB','mFyZ'),('fMB','fMZ'),('fFB','fFZ'),('fMeB','fMeZ'),('fMyB','fMyZ'),('fFeB','fFeZ'),('fFyB','fFyZ')]

### AGE DISTINGUISHED PAIRS ###

ag_pairs = [('meB','myB'),('meZ','myZ'), 
         ('mMeZeS','mMeZyS'),('mMeZeD','mMeZyD'),
         ('mMyZeS','mMyZyS'),('mMyZeD','mMyZyD'),
         ('mMZeS','mMZyS'),('mMZeD','mMZyD'),
         ('mMeBeS','mMeByS'),('mMeBeD','mMeByD'),
         ('mMyBeS','mMyByS'),('mMyBeD','mMyByD'),
         ('mMBeS','mMByS'),('mMBeD','mMByD'),
         ('mFeZeS','mFeZyS'),('mFeZeD','mFeZyD'),
         ('mFyZeS','mFyZyS'),('mFyZeD','mFyZyD'),
         ('mFZeS','mFZyS'),('mFZeD','mFZyD'),
         ('mFeBeS','mFeByS'),('mFeBeD','mFeByD'),
         ('mFyBeS','mFyByS'),('mFyBeD','mFyByD'),
         ('mFBeS','mFByS'),('mFBeD','mFByD'),
         ('mMeB','mMyB'),('mMeZ','mMyZ'),
         ('mFeB','mFyB'),('mFeZ','mFyZ'),
         ('feB','fyB'),('feZ','fyZ'), 
         ('fMeZeS','fMeZyS'),('fMeZeD','fMeZyD'),
         ('fMyZeS','fMyZyS'),('fMyZeD','fMyZyD'),
         ('fMZeS','fMZyS'),('fMZeD','fMZyD'),
         ('fMeBeS','fMeByS'),('fMeBeD','fMeByD'),
         ('fMyBeS','fMyByS'),('fMyBeD','fMyByD'),
         ('fMBeS','fMByS'),('fMBeD','fMByD'),
         ('fFeZeS','fFeZyS'),('fFeZeD','fFeZyD'),
         ('fFyZeS','fFyZyS'),('fFyZeD','fFyZyD'),
         ('fFZeS','fFZyS'),('fFZeD','fFZyD'),
         ('fFeBeS','fFeByS'),('fFeBeD','fFeByD'),
         ('fFyBeS','fFyByS'),('fFyBeD','fFyByD'),
         ('fFBeS','fFByS'),('fFBeD','fFByD'),
         ('fMeB','fMyB'),('fMeZ','fMyZ'),
         ('fFeB','fFyB'),('fFeZ','fFyZ')]

ag_gN = [('meB','myB'),('meZ','myZ'), 
         ('mMeZeS','mMeZyS'),('mMeZeD','mMeZyD'),
         ('mMyZeS','mMyZyS'),('mMyZeD','mMyZyD'),
         ('mMZeS','mMZyS'),('mMZeD','mMZyD'),
         ('mMeBeS','mMeByS'),('mMeBeD','mMeByD'),
         ('mMyBeS','mMyByS'),('mMyBeD','mMyByD'),
         ('mMBeS','mMByS'),('mMBeD','mMByD'),
         ('mFeZeS','mFeZyS'),('mFeZeD','mFeZyD'),
         ('mFyZeS','mFyZyS'),('mFyZeD','mFyZyD'),
         ('mFZeS','mFZyS'),('mFZeD','mFZyD'),
         ('mFeBeS','mFeByS'),('mFeBeD','mFeByD'),
         ('mFyBeS','mFyByS'),('mFyBeD','mFyByD'),
         ('mFBeS','mFByS'),('mFBeD','mFByD'),
         ('feB','fyB'),('feZ','fyZ'), 
         ('fMeZeS','fMeZyS'),('fMeZeD','fMeZyD'),
         ('fMyZeS','fMyZyS'),('fMyZeD','fMyZyD'),
         ('fMZeS','fMZyS'),('fMZeD','fMZyD'),
         ('fMeBeS','fMeByS'),('fMeBeD','fMeByD'),
         ('fMyBeS','fMyByS'),('fMyBeD','fMyByD'),
         ('fMBeS','fMByS'),('fMBeD','fMByD'),
         ('fFeZeS','fFeZyS'),('fFeZeD','fFeZyD'),
         ('fFyZeS','fFyZyS'),('fFyZeD','fFyZyD'),
         ('fFZeS','fFZyS'),('fFZeD','fFZyD'),
         ('fFeBeS','fFeByS'),('fFeBeD','fFeByD'),
         ('fFyBeS','fFyByS'),('fFyBeD','fFyByD'),
         ('fFBeS','fFByS'),('fFBeD','fFByD')]

ag_gN1 = [('mMeB','mMyB'),('mMeZ','mMyZ'),
         ('mFeB','mFyB'),('mFeZ','mFyZ'),
         ('fMeB','fMyB'),('fMeZ','fMyZ'),
         ('fFeB','fFyB'),('fFeZ','fFyZ')]


### SIDE DISTINGUISHED PAIRS ###

si_pairs = [('mMeZeS','mFeZeS'),('mMeZeD','mFeZeD'),
           ('mMeZyS','mFeZyS'),('mMeZyD','mFeZyD'),
           ('mMyZeS','mFyZeS'),('mMyZeD','mMyFeD'),
           ('mMyZyS','mFyZyS'),('mMyZyD','mFyZyD'),
           ('mMZeS','mFZyS'),('mMZeD','mFZyD'),
           ('mMeBeS','mFeBeS'),('mMeBeD','mFeBeD'),
           ('mMeByS','mFeByS'),('mMeByD','mFeByD'),
           ('mMyBeS','mFyBeS'),('mMyBeD','mFyBeD'),
           ('mMyByS','mFyByS'),('mMyByD','mFyByD'),
           ('mMBeS','mFByS'),('mMBeD','mFByD'),
           ('mMBD','mFBD'),('mMBS','mFBS'),
           ('mMZD','mFZD'),('mMZS','mFZS'),
           ('mMB','mFB'), ('mMZ','mFZ'),
           ('mMeB','mFeB'),('mMeZ','mFeZ'),
           ('mMyB','mFyB'),('mMyZ','mFyZ'),
           ('fMeZeS','fFeZeS'),('fMeZeD','fFeZeD'),
           ('fMeZyS','fFeZyS'),('fMeZyD','fFeZyD'),
           ('fMyZeS','fFyZeS'),('fMyZeD','fMyFeD'),
           ('fMyZyS','fFyZyS'),('fMyZyD','fFyZyD'),
           ('fMZeS','fFZyS'),('fMZeD','fFZyD'),
           ('fMeBeS','fFeBeS'),('fMeBeD','fFeBeD'),
           ('fMeByS','fFeByS'),('fMeByD','fFeByD'),
           ('fMyBeS','fFyBeS'),('fMyBeD','fFyBeD'),
           ('fMyByS','fFyByS'),('fMyByD','fFyByD'),
           ('fMBeS','fFByS'),('fMBeD','fFByD'),
           ('fMBD','fFBD'),('fMBS','fFBS'),
           ('fMZD','fFZD'),('fMZS','fFZS'),
           ('fMB','fFB'), ('fMZ','fFZ'),
           ('fMeB','fFeB'),('fMeZ','fFeZ'),
           ('fMyB','fFyB'),('fMyZ','fFyZ')]

si_gN =  [('mMeZeS','mFeZeS'),('mMeZeD','mFeZeD'),
           ('mMeZyS','mFeZyS'),('mMeZyD','mFeZyD'),
           ('mMyZeS','mFyZeS'),('mMyZeD','mMyFeD'),
           ('mMyZyS','mFyZyS'),('mMyZyD','mFyZyD'),
           ('mMZeS','mFZyS'),('mMZeD','mFZyD'),
           ('mMeBeS','mFeBeS'),('mMeBeD','mFeBeD'),
           ('mMeByS','mFeByS'),('mMeByD','mFeByD'),
           ('mMyBeS','mFyBeS'),('mMyBeD','mFyBeD'),
           ('mMyByS','mFyByS'),('mMyByD','mFyByD'),
           ('mMBeS','mFByS'),('mMBeD','mFByD'),
           ('mMBD','mFBD'),('mMBS','mFBS'),
           ('mMZD','mFZD'),('mMZS','mFZS'),
          ('fMeZeS','fFeZeS'),('fMeZeD','fFeZeD'),
           ('fMeZyS','fFeZyS'),('fMeZyD','fFeZyD'),
           ('fMyZeS','fFyZeS'),('fMyZeD','fMyFeD'),
           ('fMyZyS','fFyZyS'),('fMyZyD','fFyZyD'),
           ('fMZeS','fFZyS'),('fMZeD','fFZyD'),
           ('fMeBeS','fFeBeS'),('fMeBeD','fFeBeD'),
           ('fMeByS','fFeByS'),('fMeByD','fFeByD'),
           ('fMyBeS','fFyBeS'),('fMyBeD','fFyBeD'),
           ('fMyByS','fFyByS'),('fMyByD','fFyByD'),
           ('fMBeS','fFByS'),('fMBeD','fFByD'),
           ('fMBD','fFBD'),('fMBS','fFBS'),
           ('fMZD','fFZD'),('fMZS','fFZS')]

si_gN1 = [('mMB','mFB'), ('mMZ','mFZ'),
           ('mMeB','mFeB'),('mMeZ','mFeZ'),
           ('mMyB','mFyB'),('mMyZ','mFyZ'),
           ('fMB','fFB'), ('fMZ','fFZ'),
           ('fMeB','fFeB'),('fMeZ','fFeZ'),
           ('fMyB','fFyB'),('fMyZ','fFyZ')]

### INTERNAL CO-SELECTING PAIRS ###

ics_pairs = [#('mM','mB'),
             ('mM','meB'),('mM','myB'), #mother and siblings
             #('mM','mZ'),
             ('mM','meZ'),('mM','myZ'),
             #('mF','mB'),
             ('mF','meB'),('mF','myB'), #father and siblings
             #('mF','mZ'),
             ('mF','meZ'),('mF','myZ'),
             #('mMB','mMBS'),('mMB','mMBeS'),('mMB','mMByS'),('mMB','mMBD'),('mMB','mMBeD'),('mMB','mMByD'), #mother's brother
             ('mMeB','mMeBS'),('mMeB','mMeBeS'),('mMeB','mMeByS'),('mMeB','mMeBD'),('mMeB','mMeBeD'),('mMeB','mMeByD'), 
             ('mMyB','mMyBS'),('mMyB','mMyBeS'),('mMyB','mMyByS'),('mMyB','mMyBD'),('mMyB','mMyBeD'),('mMyB','mMyByD'), 
             #('mFB','mFBS'),('mFB','mFBeS'),('mFB','mFByS'),('mFB','mFBD'),('mFB','mFBeD'),('mFB','mFByD'), # father's brother
             ('mFeB','mFeBS'),('mFeB','mFeBeS'),('mFeB','mFeByS'),('mFeB','mFeBD'),('mFeB','mFeBeD'),('mFeB','mFeByD'),
             ('mFyB','mFyBS'),('mFyB','mFyBeS'),('mFyB','mFyByS'),('mFyB','mFyBD'),('mFyB','mFyBeD'),('mFyB','mFyByD'),
             #('mMZ','mMZS'),('mMZ','mMZeS'),('mMZ','mMZyS'),('mMZ','mMZD'),('mMZ','mMZeD'),('mMZ','mMZyD'), #mother's sister
             ('mMeZ','mMeZS'),('mMeZ','mMeZeS'),('mMeZ','mMeZyS'),('mMeZ','mMeZD'),('mMeZ','mMeZeD'),('mMeZ','mMeZyD'), 
             ('mMyZ','mMyZS'),('mMyZ','mMyZeS'),('mMyZ','mMyZyS'),('mMyZ','mMyZD'),('mMyZ','mMyZeD'),('mMyZ','mMyZyD'), 
             #('mFZ','mFZS'),('mFZ','mFZeS'),('mFZ','mFZyS'),('mFZ','mFZD'),('mFZ','mFZeD'),('mFZ','mFZyD'), # father's sister
             ('mFeZ','mFeZS'),('mFeZ','mFeZeS'),('mFeZ','mFeZyS'),('mFeZ','mFeZD'),('mFeZ','mFeZeD'),('mFeZ','mFeZyD'),
             ('mFyZ','mFyZS'),('mFyZ','mFyZeS'),('mFyZ','mFyZyS'),('mFyZ','mFyZD'),('mFyZ','mFyZeD'),('mFyZ','mFyZyD'),
             #('mM','fB'),
             ('fM','feB'),('fM','fyB'), # mother and siblings
             #('mM','fZ'),
             ('fM','feZ'),('fM','fyZ'),
             #('mF','fB'),
             ('fF','feB'),('fF','fyB'), # father and siblings
             #('mF','fZ'),
             ('fF','feZ'),('fF','fyZ'),
             #('fMB','fMBS'),('fMB','fMBeS'),('fMB','fMByS'),('fMB','fMBD'),('fMB','fMBeD'),('fMB','fMByD'), #mother's brother
             ('fMeB','fMeBS'),('fMeB','fMeBeS'),('fMeB','fMeByS'),('fMeB','fMeBD'),('fMeB','fMeBeD'),('fMeB','fMeByD'), 
             ('fMyB','fMyBS'),('fMyB','fMyBeS'),('fMyB','fMyByS'),('fMyB','fMyBD'),('fMyB','fMyBeD'),('fMyB','fMyByD'), 
             #('fFB','fFBS'),('fFB','fFBeS'),('fFB','fFByS'),('fFB','fFBD'),('fFB','fFBeD'),('fFB','fFByD'), # father's brother
             ('fFeB','fFeBS'),('fFeB','fFeBeS'),('fFeB','fFeByS'),('fFeB','fFeBD'),('fFeB','fFeBeD'),('fFeB','fFeByD'),
             ('fFyB','fFyBS'),('fFyB','fFyBeS'),('fFyB','fFyByS'),('fFyB','fFyBD'),('fFyB','fFyBeD'),('fFyB','fFyByD'),
             #('fMZ','fMZS'),('fMZ','fMZeS'),('fMZ','fMZyS'),('fMZ','fMZD'),('fMZ','fMZeD'),('fMZ','fMZyD'), #mother's sister
             ('fMeZ','fMeZS'),('fMeZ','fMeZeS'),('fMeZ','fMeZyS'),('fMeZ','fMeZD'),('fMeZ','fMeZeD'),('fMeZ','fMeZyD'), 
             ('fMyZ','fMyZS'),('fMyZ','fMyZeS'),('fMyZ','fMyZyS'),('fMyZ','fMyZD'),('fMyZ','fMyZeD'),('fMyZ','fMyZyD'), 
             #('fFZ','fFZS'),('fFZ','fFZeS'),('fFZ','fFZyS'),('fFZ','fFZD'),('fFZ','fFZeD'),('fFZ','fFZyD'), # father's sister
             ('fFeZ','fFeZS'),('fFeZ','fFeZeS'),('fFeZ','fFeZyS'),('fFeZ','fFeZD'),('fFeZ','fFeZeD'),('fFeZ','fFeZyD'),
             ('fFyZ','fFyZS'),('fFyZ','fFyZeS'),('fFyZ','fFyZyS'),('fFyZ','fFyZD'),('fFyZ','fFyZeD'),('fFyZ','fFyZyD')]


# ics_pairs = [('mMeB','mMeBS'),('mMeB','mMeBD'),('mMeZ','mMeZS'),('mMeZ','mMeZD'),('mFeB','mFeBS'),('mFeB','mFeBD'),('mFeZ','mFeZS'),('mFeZ','mFeZD'),('mMyB','mMyBS'),('mMyB','mMyBD'),('mMyZ','mMyZS'),('mMyZ','mMyZD'),('mFyB','mFyBS'),('mFyB','mFyBD'),('mFyZ','mFyZS'),('mFyZ','mFyZD')]






