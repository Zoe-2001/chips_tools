import cc_dat_utils as cc

#Part 1
input_dat_file = "data/pfgd_test.dat"



if __name__ == "__main__":
    # Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file
    output_cc_level_object = cc.make_cc_level_pack_from_dat(input_dat_file)

    # print the resulting data
    print(output_cc_level_object)