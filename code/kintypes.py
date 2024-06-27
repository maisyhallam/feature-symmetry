ics_pairs = [

# parents and siblings

('mM','meB'),('mM','myB'), ('mF','meB'),('mF','myB'),
('mM','meZ'),('mM','myZ'), ('mF','meZ'),('mF','myZ'),
('fM','feB'),('fM','fyB'), ('fF','feB'),('fF','fyB'),
('fM','feZ'),('fM','fyZ'), ('fF','feZ'),('fF','fyZ'),


# nuncles and cousins

# mother's brother

('mMeB','mMeBS'),('mMeB','mMeBD'),('mMyB','mMyBS'),('mMyB','mMyBD'),
('fMeB','fMeBS'),('fMeB','fMeBD'),('fMyB','fMyBS'),('fMyB','fMyBD'),

# mother's sister
    
('mMeZ','mMeZS'),('mMeZ','mMeZD'),('mMyZ','mMyZS'),('mMyZ','mMyZD'),
('fMeZ','fMeZS'),('fMeZ','fMeZD'),('fMyZ','fMyZS'),('fMyZ','fMyZD'),
    
# father's brother
    
('mFeB','mFeBS'),('mFeB','mFeBD'),('mFyB','mFyBS'),('mFyB','mFyBD'),
('fFeB','fFeBS'),('fFeB','fFeBD'),('fFyB','fFyBS'),('fFyB','fFyBD'),
    
# father's sister

('mFeZ','mFeZS'),('mFeZ','mFeZD'),('mFyZ','mFyZS'),('mFyZ','mFyZD'),
('fFeZ','fFeZS'),('fFeZ','fFeZD'),('fFyZ','fFyZS'),('fFyZ','fFyZD')

]

generation_n = [
                'meB', 'meZ',
                'myB', 'myZ',
                'mMeZS', 'mMeZD',
                'mMeBS','mMeBD',
                'mMyZS', 'mMyZD',
                'mMyBS', 'mMyBD',
                'mFeZS', 'mFeZD',
                'mFeBS', 'mFeBD',
                'mFyZS', 'mFyZD',
                'mFyBS', 'mFyBD',
                
                'feB', 'feZ',
                'fyB', 'fyZ',
                'fMeZS', 'fMeZD',
                'fMeBS','fMeBD',
                'fMyZS', 'fMyZD',
                'fMyBS', 'fMyBD',
                'fFeZS', 'fFeZD',
                'fFeBS', 'fFeBD',
                'fFyZS', 'fFyZD',
                'fFyBS', 'fFyBD']


generation_n1 = [
                 'mM','mF',
                 'mMeB','mMeZ',
                 'mMyB','mMyZ',
                 'mFeB','mFeZ',
                 'mFyB','mFyZ',
                 'fM','fF',
                 'fMeB','fMeZ',
                 'fMyB','fMyZ',
                 'fFeB','fFeZ',
                 'fFyB','fFyZ']

pairs_no_parents = [

# nuncles and cousins

# mother's brother

('mMeB','mMeBS'),('mMeB','mMeBD'),('mMyB','mMyBS'),('mMyB','mMyBD'),
('fMeB','fMeBS'),('fMeB','fMeBD'),('fMyB','fMyBS'),('fMyB','fMyBD'),

# mother's sister
    
('mMeZ','mMeZS'),('mMeZ','mMeZD'),('mMyZ','mMyZS'),('mMyZ','mMyZD'),
('fMeZ','fMeZS'),('fMeZ','fMeZD'),('fMyZ','fMyZS'),('fMyZ','fMyZD'),
    
# father's brother
    
('mFeB','mFeBS'),('mFeB','mFeBD'),('mFyB','mFyBS'),('mFyB','mFyBD'),
('fFeB','fFeBS'),('fFeB','fFeBD'),('fFyB','fFyBS'),('fFyB','fFyBD'),
    
# father's sister

('mFeZ','mFeZS'),('mFeZ','mFeZD'),('mFyZ','mFyZS'),('mFyZ','mFyZD'),
('fFeZ','fFeZS'),('fFeZ','fFeZD'),('fFyZ','fFyZS'),('fFyZ','fFyZD')

]
