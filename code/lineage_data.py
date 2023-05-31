### LINEAGE ###
types_pairs = {
'p_siblings': [('mMeB','mFeB'),('mMeZ','mFeZ'),('mMyB','mFyB'),('mMyZ','mFyZ')],
'pz_cousins': [('mMeZeS','mFeZeS'),('mMeZeD','mFeZeD'),('mMeZyS','mFeZyS'),('mMeZyD','mFeZyD'),
               ('mMyZeS','mFyZeS'),('mMyZeD','mMyFeD'),('mMyZyS','mFyZyS'),('mMyZyD','mFyZyD'),
               ('mMZeS','mFZyS'),('mMZeD','mFZyD')],
'pb_cousins': [('mMeBeS','mFeBeS'),('mMeBeD','mFeBeD'),('mMeByS','mFeByS'),('mMeByD','mFeByD'),
                ('mMyBeS','mFyBeS'),('mMyBeD','mFyBeD'),('mMyByS','mFyByS'),('mMyByD','mFyByD'),
                ('mMBeS','mFByS'),('mMBeD','mFByD')]
}

pairs = [('fMeZeS','fFeZeS'),('fMeZeD','fFeZeD'),('fMeZyS','fFeZyS'),('fMeZyD','fFeZyD'),
         ('fMyZeS','fFyZeS'),('fMyZeD','fMyFeD'),('fMyZyS','fFyZyS'),('fMyZyD','fFyZyD'),
         ('fMZeS','fFZyS'),('fMZeD','fFZyD'),('fMeBeS','fFeBeS'),('fMeBeD','fFeBeD'),('fMeByS','fFeByS'),
         ('fMeByD','fFeByD'),('fMyBeS','fFyBeS'),('fMyBeD','fFyBeD'),('fMyByS','fFyByS'),('fMyByD','fFyByD'),
         ('fMBeS','fFByS'),('fMBeD','fFByD'),('fMBD','fFBD'),('fMBS','fFBS'),('fMZD','fFZD'),('fMZS','fFZS'),
         ('fMB','fFB'), ('fMZ','fFZ'),('fMeB','fFeB'),('fMeZ','fFeZ'),('fMyB','fFyB'),('fMyZ','fFyZ')]

generation1_pairs = [('mMeZeS','mFeZeS'),('mMeZeD','mFeZeD'),('mMeZyS','mFeZyS'),('mMeZyD','mFeZyD'),
               ('mMyZeS','mFyZeS'),('mMyZeD','mMyFeD'),('mMyZyS','mFyZyS'),('mMyZyD','mFyZyD'),
               ('mMZeS','mFZyS'),('mMZeD','mFZyD'),('mMeBeS','mFeBeS'),('mMeBeD','mFeBeD'),('mMeByS','mFeByS'),('mMeByD','mFeByD'),
               ('mMyBeS','mFyBeS'),('mMyBeD','mFyBeD'),('mMyByS','mFyByS'),('mMyByD','mFyByD'),
               ('mMBeS','mFByS'),('mMBeD','mFByD'),('mMBD','mFBD'),('mMBS','mFBS'),('mMZD','mFZD'),('mMZS','mFZS')]

generation2_pairs = [('mMB','mFB'), ('mMZ','mFZ'),('mMeB','mFeB'),('mMeZ','mFeZ'),('mMyB','mFyB'),('mMyZ','mFyZ')]

kin_types = ['p_siblings','pz_cousins','pb_cousins']

generation1 = ['pz_cousins','pb_cousins']
generation2 = ['p_siblings']
