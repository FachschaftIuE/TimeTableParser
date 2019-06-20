from tabula import read_pdf


# Tim Brodersen
def pdf_to_json_parser():

    json_df = read_pdf("../data/input/4_ini_3.pdf", output_format="json")
    print("Tim Brodersen (Hello World!):")
    print(json_df)
