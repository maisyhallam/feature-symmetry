import sys
import csv
import os
import gender_data as ge
import age_data as age
import lineage_data as li
from collections import Counter


def get_kin(file_path):
    """Loads in a csv file, populates a dictionary with the kin terms."""
    kin_terms = {}
    with open(file_path, encoding="utf8") as f:
        csv_reader = csv.DictReader(f)
        for line in csv_reader:
            parameter = line['parameter'] # kin type
            word = line['word'] # kin term
            kin_terms[parameter] = word
    return kin_terms

def denominator(generation_list,feature,number):
    """Returns the number of possible relationships that could have this distinction."""
    denominator = 0

    if feature == 'gender':
        for kin_type in generation_list:
            for pair in ge.pairs[kin_type]:
                denominator += 1
        denominator -= number

    elif feature == 'age':
        for kin_type in generation_list:
            for pair in age.pairs[kin_type]:
                denominator += 1
        denominator -= number

    elif feature == 'lineage':
        for kin_type in generation_list:
            for pair in li.pairs[kin_type]:
                denominator += 1
        denominator -= number

    else:
        print('Not a valid feature.')

    return denominator

def check_feature_symmetry(ks,feature):
    """Checks whether the terms used in the language for each pair of kin terms match."""
    results = {}

    if feature == 'gender':

        for pair in ge.pairs:
            if pair[0] in ks.keys() and pair[1] in ks.keys():
                if ks[pair[0]] == ks[pair[1]]:
                    results[pair] = 0
                else:
                    results[pair] = 1
            else:
                results[pair] = 'null'
        # for kin in ge.kin_types:
        #     count = 0
        #     for pair in ge.pairs[kin]:
        #         if pair[0] in ks.keys() and pair[1] in ks.keys():
        #             if ks[pair[0]] == ks[pair[1]]:
        #                 results[pair] = 0
        #             else:
        #                 results[pair] = 1
        #         else:
        #             results[pair] = 'null'

    elif feature == 'age':

        for pair in age.pairs:
                if pair[0] in ks.keys() and pair[1] in ks.keys():
                    if ks[pair[0]] == ks[pair[1]]:
                        results[pair] = 0
                    else:
                        results[pair] = 1
                else:
                    results[pair] = 'null'

    elif feature == 'lineage':

        for pair in li.pairs:
                if pair[0] in ks.keys() and pair[1] in ks.keys():
                    if ks[pair[0]] == ks[pair[1]]:
                        results[pair] = 0
                    else:
                        results[pair] = 1
                else:
                    results[pair] = 'null'

    else:
        print('Not a valid feature.')

    return results

def get_csv_files(path):
    """Fetches a list of files from the directory located by the given filepath."""
    directory = os.scandir(path)
    files = []
    for file in directory:
        files.append(file.name)
    return files

def get_language_name(string):
    """Extract the language name from the filename of kinbank data."""
    language_name = ''
    if string.startswith('Morgan1871_'):
        string = string[len('Morgan1871_'):]
    for i in range(len(string)-13):
        language_name += string[i]
    return language_name


def write_symmetry_csv(filename,file,symmetries):
    """Writes a csv file with the name of each frankenlanguage file plus its symmetry score."""
    with open(filename, 'a', encoding="utf8") as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow([file] + symmetries)

def generation_results(feature_symmetry_results,feature):
    """Returns the proportion of feature distinctions for each generation: number of
     feature distinctions made over the total number of distinctions available.
     A score is 'null' if there weren't any minimal pairs in the data (so unable to tell)."""
    results = {}
    gen1_values = []
    gen2_values = []

    if feature == 'gender':
        for i in feature_symmetry_results:
            if i in ge.generation1_pairs:
                gen1_values.append(feature_symmetry_results[i])
            else:
                gen2_values.append(feature_symmetry_results[i])

    elif feature == 'age':
        for i in feature_symmetry_results:
            if i in age.generation1_pairs:
                gen1_values.append(feature_symmetry_results[i])
            else:
                gen2_values.append(feature_symmetry_results[i])

    elif feature == 'lineage':
        for i in feature_symmetry_results:
            if i in li.generation1_pairs:
                gen1_values.append(feature_symmetry_results[i])
            else:
                gen2_values.append(feature_symmetry_results[i])

        # unsure whether to keep this or not - seems unfair either way to count or not count where there isn't enough data to know for sure if a distinction is made
    gen1_values = [x for x in gen1_values if x != 'null']
    gen2_values = [x for x in gen2_values if x != 'null']

    gen1_denominator = len(gen1_values) # denominator(ge.generation1,feature,gen1_nulls)
    gen2_denominator = len(gen2_values) # denominator(ge.generation2,feature,gen2_nulls)

    if gen1_denominator == 0:
        results['generation1'] = 'null'
    else:
        results['generation1'] = sum(gen1_values)/gen1_denominator

    if gen2_denominator == 0:
        results['generation2'] = 'null'
    else:
        results['generation2'] = sum(gen2_values)/gen2_denominator

    return results



def write_full_csv(filename,language,generation_results,set,type):
    """Creates a list of a languages two generation scores, and writes the language name + score to a csv file if the score != 'null'."""
    generation1 = generation_results['generation1']
    generation2 = generation_results['generation2']
    if generation1 == 'null' or generation2 == 'null':
        pass
    else:
        with open(filename, 'a', encoding='utf8') as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow([language,generation1,generation2,set,type])

def write_headers(filename):
    with open(filename, 'a', encoding='utf8') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(['language','gen0','gen1','set','data_type'])

def main(data_type,count,feature):
    if data_type == 'kinbank':
        #filename = '../data/raw/' + feature + '/prop/kinbank.csv'
        filename = '../test/data/kinbank_test.csv'
        file_path = '../languages/kinbank/'
        write_headers(filename)

        files = get_csv_files(file_path)

        for file in files:
            ks = get_kin(file_path + file)
            language = get_language_name(file)
            feature_symmetry_results = check_feature_symmetry(ks,feature)
            gen_results = generation_results(feature_symmetry_results,feature)

            write_full_csv(filename,language,gen_results,'kinbank','kinbank') # family) #

    # if data_type == 'family':
    #     for family in families:
    #         files = get_csv_files('../kinbank/raw/' + family)
    #         filename = '../data/' + feature + '/prop/families/kinbank_' + family + '.csv'
    #         write_headers(filename)
    #         for file in files:
    #             ks = get_kin('../kinbank/raw/' + family + '/' + file,'parameter','word')
    #             language = get_language_name(file)
    #             feature_symmetry_results = check_feature_symmetry(ks,feature)
    #             gen_results = generation_results(feature_symmetry_results,feature)
    #
    #             write_full_csv(filename,language,gen_results,family)

    if data_type == 'frankenlanguage':
        file_path = '../languages/frankenlanguages/'
        directory_counter = 0
        filename = '../test/data/frankenlanguage_test.csv'
        write_headers(filename)

        for i in range(int(count)):
            directory_counter += 1
            #filename = '../data/raw/' + feature + '/prop/simulation' + str(directory_counter) + '.csv'
            #files = get_csv_files(file_path + str(directory_counter))
            files = get_csv_files('../test/languages/' + str(directory_counter))

            for file in files:
                #ks = get_kin(file_path + str(directory_counter) + '/' + file,'TYPE','TERM')
                ks = get_kin('../test/languages/' + str(directory_counter) + '/' + file)
                feature_symmetry_results = check_feature_symmetry(ks,feature)
                gen_results = generation_results(feature_symmetry_results,feature)
                language = file + '_' + str(directory_counter)

                write_full_csv(filename,language,gen_results,str(directory_counter),'frankenlanguage')

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2],sys.argv[3])
