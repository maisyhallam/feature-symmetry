""" This script generates 'frankenlanguages' from crosslinguistic data on the
structure of kinship systems, using the KinBank data (www.kinbank.net).

Making a frankenlanguage involves taking the kin terms from Generation 0 of
one kinship system and the kin terms from Generation +1 of another kinship
system, and then stitching them together - hence the reference to frankenstein's monster.

I've done this in order to work out whether there are statistical regularities
in the patterns of kinship systems crosslinguistically - by running my analysis
on the frankenlanguages I am able to work out how likely it is that a kinship
system would exhibit these regularities entirely by chance.

This script only uses sibling and cousin terminology from generation 0 (ego's
generation) and generation +1 (ego's parents' generation) to generate the
frankenlanguages. """

import sys
import csv
import os
import random

# shorthand for kin types in Ego's generation
generation_n = ['mB','mZ',
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
                'mFBeS','mFBeD','mFByS','mFByD','mFBS','mFBD']

# shorthand for kin types in Ego's parents' generation
generation_n1 = ['mMB','mMZ',
                 'mFB','mFZ',
                 'mMeB','mMeZ',
                 'mMyB','mMyZ',
                 'mFeB','mFeZ',
                 'mFyB','mFyZ']

def get_csv_files():
    """Creates a dictionary where keys are language families (directories) and values are kinbank filenames."""
    files = []
    path = '../languages/kinbank'
    directory = os.scandir(path)
    for file in directory:
        files.append(file.name)
    print(len(files))
    return files

def get_kin(file):
    """Loads in a csv file from the kinbank data, populates a dictionary with the kin terms from that csv."""
    file_path = '../languages/kinbank/' + file
    kin_terms = {}
    with open(file_path, encoding="utf8") as f:
        csv_reader = csv.DictReader(f)
        next(csv_reader) # skip the header
        for line in csv_reader:
            parameter = line['parameter'] # relationship
            word = line['word'] # kin term
            kin_terms[parameter] = word
    return kin_terms


all_language_data = get_csv_files()

def two_random_languages(all_data):
    """Picks two random entries from the dictionary created by get_csv_files()
    and returns a tuple of directory,filename for each."""
    language1 = random.choice(all_data)
    language2 = random.choice(all_data)
    print(language1,language2)
    # if language1[1] != language2[1]:
    #     return language1,language2
    # else:
    #     return two_random_languages(all_data)
    return language1,language2

# def finalise_frankenlanguage(all_data,g1,g2):
#     if not g1 or not g2:
#         return create_frankenlanguage(all_data)
#     else:
#         frankenlanguage = {**g1, **g2} # combine two dictionaries
#         return frankenlanguage

def create_frankenlanguage(all_data):
    """For two random files in the kinbank data, splits the terms by generation and
    re-combines them to create a dictionary where the keys are kin types and the
    values are kin terms, such that one generation of terms comes from one language
    and the other generation comes from another language."""
    language1,language2 = two_random_languages(all_data)
    language1_terms = get_kin(language1)
    language2_terms = get_kin(language2)
    g1 = {}
    g2 = {}

    for type in language1_terms.keys():
        if type in generation_n:
            g1[type] = language1_terms[type]
        else:
            continue

    for type in language2_terms.keys():
        if type in generation_n1:
            g2[type] = language2_terms[type]
        else:
            continue

    frankenlanguage = {**g1, **g2} # combine two dictionaries
    return(frankenlanguage)


    #return finalise_frankenlanguage(all_data,generation_n_terms,generation_n1_terms)



def write_frankenlanguage_to_csv(frankenlanguage,filename):
    """Writes each kin type and kin term from the frankenlanguage to a new csv file."""
    with open(filename, 'a', encoding="utf8") as csv_file:
        csvwriter = csv.writer(csv_file)
        write_headers(filename)
        for type in frankenlanguage.keys():
            csvwriter.writerow([type,frankenlanguage[type]])

def write_headers(file):
    """Write the headers to the CSV file."""
    with open(file, 'a') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(['parameter','word'])

def main(times,number_languages):
    directory_counter = 0

    for i in range(int(times)):
        filename_counter = 0
        directory_counter += 1
        file_path = '../test/languages/'+ str(directory_counter)
        os.mkdir(file_path)

        # os.mkdir('../languages/frankenlanguages/' + str(directory_counter))
        # create n frankenlanguages and save them to individual csvs
        for i in range(int(number_languages)):
            filename_counter += 1
            frankenlanguage = create_frankenlanguage(all_language_data)
            write_frankenlanguage_to_csv(frankenlanguage,file_path + '/frankenlanguage' + str(filename_counter) + '.csv') # write_frankenlanguage_to_csv(frankenlanguage,'../frankenlanguages/' + str(directory_counter) + '/frankenlanguage' + str(filename_counter) + '.csv')

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
