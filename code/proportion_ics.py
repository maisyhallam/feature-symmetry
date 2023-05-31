import sys
import csv
import os
from collections import Counter
import pprint
pp = pprint.PrettyPrinter(indent=4)

all_kin_types = ['mMB','mMeB','mMyB',
                 'mMZ','mMeZ','mMyZ',
                 'mFB','mFeB','mFyB',
                 'mFZ','mFeZ','mFyZ',
                 'mMBS','mMBD',
                 'mMeBS','mMeBD',
                 'mMyBS','mMyBD',
                 'mMZS','mMZD',
                 'mMeZS','mMeZD',
                 'mMyZS','mMyZD',
                 'mFBS','mFBD',
                 'mFeBS','mFeBD',
                 'mFyBS','mFyBD',
                 'mFZS','mFZD',
                 'mFeZS','mFeZD',
                 'mFyZS','mFyZD',
                 'fMB','fMeB','fMyB',
                 'fMZ','fMeZ','fMyZ',
                 'fFB','fFeB','fFyB',
                 'fFZ','fFeZ','fFyZ',
                 'fMBS','fMBD',
                 'fMeBS','fMeBD',
                 'fMyBS','fMyBD',
                 'fMZS','fMZD',
                 'fMeZS','fMeZD',
                 'fMyZS','fMyZD',
                 'fFBS','fFBD',
                 'fFeBS','fFeBD',
                 'fFyBS','fFyBD',
                 'fFZS','fFZD',
                 'fFeZS','fFeZD',
                 'fFyZS','fFyZD']

('fMB','fMBS'),('fMB','fMBeS'),('fMB','fMByS'),('fMB','fMBD'),('fMB','fMBeD'),('fMB','fMByD'),
             ('fMeB','fMeBS'),('fMeB','fMeBD'),('fMeB','fMeByS'),('fMeB','fMeBD'),('fMeB','fMeBeD'),('fMeB','fMeByD'),
             ('fMyB','fMyBS'),('fMyB','fMyBD'),('fMyB','fMyByS'),('fMyB','fMyBD'),('fMyB','fMyBeD'),('fMyB','fMyByD'),
             ('fFB','fFBS'),('fFB','fFBD'),('fFB','fFByS'),('fFB','fFBD'),('fFB','fFBeD'),('fFB','fFByD'),
             ('fFeB','fFeBS'),('fFeB','fFeBD'),('fFeB','fFeByS'),('fFeB','fFeBD'),('fFeB','fFeBeD'),('fFeB','fFeByD'),
             ('fFyB','fFyBS'),('fFyB','fFyBD'),('fFyB','fFyByS'),('fFyB','fFyBD'),('fFyB','fFyBeD'),('fFyB','fFyByD'),
             ('fMZ','fMZS'),('fMZ','fMZD'),('fMZ','fMZyS'),('fMZ','fMZD'),('fMZ','fMZeD'),('fMZ','fMZyD'),
             ('fMeZ','fMeZS'),('fMeZ','fMeZD'),('fMeZ','fMeZyS'),('fMeZ','fMeZD'),('fMeZ','fMeZeD'),('fMeZ','fMeZyD'),
             ('fMyZ','fMyZS'),('fMyZ','fMyZD'),('fMyZ','fMyZyS'),('fMyZ','fMyZD'),('fMyZ','fMyZeD'),('fMyZ','fMyZyD'),
             ('fFZ','fFZS'),('fFZ','fFZD'),('fFZ','fFZyS'),('fFZ','fFZD'),('fFZ','fFZeD'),('fFZ','fFZyD'),
             ('fFeZ','fFeZS'),('fFeZ','fFeZD'),('fFeZ','fFeZyS'),('fFeZ','fFeZD'),('fFeZ','fFeZeD'),('fFeZ','fFeZyD'),
             ('fFyZ','fFyZS'),('fFyZ','fFyZD'),('fFyZ','fFyZyS'),('fFyZ','fFyZD'),('fFyZ','fFyZeD'),('fFyZ','fFyZyD')]

parent_child_pairs = [('mMB','mMBS'),('mMB','mMBD'),('mMeB','mMeBS'),('mMeB','mMeBD'),('mMyB','mMyBS'),('mMyB','mMyBD'),
                      ('mFB','mFBS'),('mFB','mFBD'),('mFeB','mFeBS'),('mFeB','mFeBD'),('mFyB','mFyBS'),('mFyB','mFyBD'),
                      ('mMZ','mMZS'),('mMZ','mMZD'),('mMeZ','mMeZS'),('mMeZ','mMeZD'),('mMyZ','mMyZS'),('mMyZ','mMyZD'),
                      ('mFZ','mFZS'),('mFZ','mFZD'),('mFeZ','mFeZS'),('mFeZ','mFeZD'),('mFyZ','mFyZS'),('mFyZ','mFyZD'),
                      ('fMB','fMBS'),('fMB','fMBD'),('fMeB','fMeBS'),('fMeB','fMeBD'),('fMyB','fMyBS'),('fMyB','fMyBD'),
                      ('fFB','fFBS'),('fFB','fFBD'),('fFeB','fFeBS'),('fFeB','fFeBD'),('fFyB','fFyBS'),('fFyB','fFyBD'),
                      ('fMZ','fMZS'),('fMZ','fMZD'),('fMeZ','fMeZS'),('fMeZ','fMeZD'),('fMyZ','fMyZS'),('fMyZ','fMyZD'),
                      ('fFZ','fFZS'),('fFZ','fFZD'),('fFeZ','fFeZS'),('fFeZ','fFeZD'),('fFyZ','fFyZS'),('fFyZ','fFyZD')]

# lists of relevant relationships in each gen (index of both lists gives a parent-child pair)
# male ego
gen2_m = ['mMB','mMeB','mMyB','mMZ','mMeZ','mMyZ','mFB','mFeB','mFyB','mFZ','mFeZ','mFyZ']
gen1_m = ['mMBS','mMBD' 'mMeBS', 'mMeBD','mMyBS','mMyBD','mMZS','mMZD','mMeZS','mMeZD','mMyZS',
          'mMyZD','mFBS','mFBD','mFeBS','mFeBD','mFyBS','mFyBD','mFZS','mFZD','mFeZS','mFeZD','mFyBS','mFyBD']

# female ego
gen2_f = ['fMB','fMeB','fMyB','fMZ','fMeZ','fMyZ','fFB','fFeB','fFyB','fFZ','fFeZ','fFyZ']
gen1_f = ['fMBS','fMBD' 'fMeBS', 'fMeBD','fMyBS','fMyBD','fMZS','fMZD','fMeZS','fMeZD','fMyZS',
          'fMyZD','fFBS','fFBD','fFeBS','fFeBD','fFyBS','fFyBD','fFZS','fFZD','fFeZS','fFeZD','fFyBS','fFyBD']

# list of language families, ie directory names that the kinbank data is divided into
families = ['Austroasiatic', 'Sino-Tibetan', 'Afro-Asiatic',
'Indo-European', 'Pano-Tacanan', 'Nuclear Trans New Guinea',
'Pama-Nyungan', 'Tai-Kadai', 'Other', 'Arawakan', 'Austronesian', 'Algic',
'Cariban', 'Nakh-Daghestanian', 'Turkic', 'Dravidian', 'Uto-Aztecan',
'Atlantic-Congo', 'Uralic', 'Tupian']

def get_kin(file_path,type,term):
    """Loads in a language csv file, populates a dictionary with the kin terms."""
    kin_terms = {}
    with open(file_path, encoding="utf8") as f:
        csv_reader = csv.DictReader(f)
        for line in csv_reader:
            parameter = line[type] # kin type
            word = line[term] # kin term
            kin_terms[parameter] = word
    return kin_terms

def get_csv_files(path):
    """Returns a list of csv filenames."""
    directory = os.scandir(path)
    files = []
    for file in directory:
        files.append(file.name)
    return files

def list_kin(ks):
    """Returns a dict of the relevant kin terms for each kin type, na if not available in the data."""
    all_kin_terms = {}

    for kin_type in all_kin_types:
        if kin_type in ks.keys():
            all_kin_terms[kin_type] = ks[kin_type]

    pp.pprint(all_kin_terms)
    print(len(all_kin_terms))
    return all_kin_terms


# def code_kin_types(ks):
#     all_kin = list_kin(ks)
#     codes = {}
#     placeholder = []
#     code = 0
#
#     # code each unique item in gen_pattern
#     for kin_type in all_kin_types:
#         if kin_type in placeholder:
#             continue
#         elif all_kin[kin_type] == 'na':
#             codes[kin_type] = 0
#         else:
#             placeholder.append(kin_type)
#             code += 1
#             codes[kin_type] = code # so looks like mB: 1, for instance
#
#     print(codes)
    #
    # return codes

def count_codes(ks):
    """Check how many times each term appears in a parent-child pair."""
    all_kin_terms = list_kin(ks)
    coded_pairs = []

#    for i in range(len(parent_child_pairs)):

    for pair in parent_child_pairs:
        if pair[0] in all_kin_terms and pair[1] in all_kin_terms:
            coded_pairs.append((all_kin_terms[pair[0]],all_kin_terms[pair[1]]))


    counts_of_pairs = Counter(coded_pairs)
    pp.pprint(counts_of_pairs)

    return counts_of_pairs,all_kin_terms


def ics_score(ks):
    # codes = code_kin_types(ks)
    counts_of_pairs,all_kin_terms = count_codes(ks)

    if len(counts_of_pairs) == 0:
        pass
    else:
        score = 1 / len(counts_of_pairs)
        print(score)
        return score


# def enumerate_generation(gen):
#     """Turn lists of kin terms into lists of numbers. Each number indicates a unique kin term."""
#     codes = code_kin_types(gen)
#     code = 0
#
#     gen_pattern = [i for i in gen]
#
#
#     for kin_type in set(gen_pattern):
#
#         while kin_type in gen_pattern:
#             index = gen_pattern.index(kin_type)
#
#             # label it 0 if na, or otherwise unspecified in the original data
#             if kin_type == 'na' or kin_type == '0' or kin_type == "":
#                 gen_pattern[index] = 0
#             # give it a unique number if anything else
#             else:
#                 gen_pattern[index] = codes[kin_type]
#
#     return gen_pattern
#
# def ICS_score(pattern1,pattern2):
#     """Checks whether the categories of kin are the same in gen2 as gen1."""
#     ICS_score = 0
#     denominator = len(gen1)
#
#     # for each type of kin
#     for i in range(len(gen1)):
#         if pattern1[i] == 0 or pattern2[i] == 0:
#             denominator -= 1
#         elif pattern1[i] == pattern2[i]:
#             ICS_score += 1
#         else:
#             pass
#
#     all_data = pattern1 + pattern2
#
#     # # if all of one generation is identical, automatic co-selection
#     # if len(set(pattern1)) == 1 or len(set(pattern2)) == 1:
#     #     ICS_score = denominator
#
#     # if there is no data for one of the generations, exclude this language
#     if sum(pattern1) == 0 or sum(pattern2) == 0:
#         pass
#     # if there is no data for any of the relevant relationships, exclude this language
#     elif denominator == 0:
#         pass
#     # if more than half the data is missing, exclude this language
#     elif all_data.count(0) > 12:
#         pass
#     else:
#         return (ICS_score/denominator)

def write_headers(filename):
    file_path = '../data/raw/ICS/' + filename + '.csv'
    with open(file_path, 'a', encoding='utf8') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(['LANGUAGE','SCORE'])

def write_full_csv(filename,language,score):
    """Writes the language, proportion of ICS, and each kin type's kin term to a csv file"""
    file_path = '../data/raw/ICS/' + filename + '.csv'
    row = [language] + [score]

    with open(file_path, 'a', encoding='utf8') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(row)

def get_language_name(string):
    """Extract the language name from the filename of kinbank data."""
    language_name = ''
    if string.startswith('Morgan1871_'):
        string = string[len('Morgan1871_'):]
    for i in range(len(string)-13):
        language_name += string[i]
    return language_name


def main(data_type,count):
    """Data_type is kinbank or frankenlanguage,count is the number of iterations (1000 for franken)."""
    if data_type == 'kinbank':
        write_headers(data_type)
        for family in families:
            files = get_csv_files('../kinbank/raw/' + family)

            for file in files:
                print(file)
                ks = get_kin('../kinbank/raw/' + family + '/' + file,'parameter','word')
                score = ics_score(ks)
                language = get_language_name(file)
                write_full_csv(data_type,language,score)
                # ks = get_kin('../kinbank/raw/' + family + '/' + file,'parameter','word')
                # language = get_language_name(file)
                # generation1 = list_generations(ks,gen1)
                # generation2 = list_generations(ks,gen2)
                # gen1_pattern = enumerate_generation(generation1)
                # gen2_pattern = enumerate_generation(generation2)
                # score = ICS_score(gen1_pattern,gen2_pattern)
                # if score:
                #     write_full_csv(data_type,language,generation1,generation2,score)
                # else:
                #     pass
    if data_type == 'frankenlanguage':
        directory_counter = 0
        for i in range(int(count)):
            directory_counter += 1
            files = get_csv_files('../frankenlanguages/' + str(directory_counter))
            write_headers(data_type + '_' + str(directory_counter))

            for file in files:
                ks = get_kin('../frankenlanguages/' + str(directory_counter) + '/' + file,'TYPE','TERM')
                language = file + '_' + str(directory_counter)
                generation1 = list_generations(ks,gen1)
                generation2 = list_generations(ks,gen2)
                gen1_pattern = enumerate_generation(generation1)
                gen2_pattern = enumerate_generation(generation2)
                score = ICS_score(gen1_pattern,gen2_pattern)
                if score:
                    write_full_csv(data_type + '_' + str(directory_counter),language,generation1,generation2,score)
                else:
                    pass

    if data_type == 'test':
        file = '../kinbank/raw/Austronesian/Araki_arak1252.csv'
        ks = get_kin(file,'parameter','word')
        score = ics_score(ks)
        language = get_language_name(file)
        # write_full_csv(data_type,language,score)




    # directory_counter = 0
    #
    # for i in range(int(argv)):
    #     directory_counter += 1
    #     files = get_csv_files('../frankenlanguages/' + str(directory_counter))
    #     write_headers('../data/frankenlanguages_ICS.csv')
    #
    #     for file in files:
    #         kin_terms = get_kin(file,str(directory_counter))
    #         feature_symmetry_results = check_feature_symmetry(kin_terms)
    #         gen_results = generation_results(feature_symmetry_results)
    #
    #         write_full_csv('../data/frankenlanguages_ICS.csv',file + '_' + str(directory_counter),gen_results)

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])

# ks = get_kin('English_stan1293.csv','Indo-European')
# generation1 = list_generations(ks,gen1)
# generation2 = list_generations(ks,gen2)
# print(generation1)
# gen1_pattern = enumerate_generation(generation1)
# gen2_pattern = enumerate_generation(generation2)
# print(generation1)
#
#
# # print(gen1_pattern,gen2_pattern)
# score = ICS_score(gen1_pattern,gen2_pattern)
# write_full_csv('English','English',generation1,generation2,score)
