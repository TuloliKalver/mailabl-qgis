from .settings import Filepaths

icon_paths = Filepaths()

open_folder = ":/oauth2method/svg/fileopen.svg"
digidoc_file = icon_paths.digi_doc_icon()
universal_file = ":/qt-project.org/styles/commonstyle/images/filelink-128.png"
pdf_file = ":/images/themes/default/mActionSaveAsPDF.svg"



class iconHandler:
    @staticmethod
    def setIcon(dokLink):

        # Check for a file extension (e.g., '.pdf', '.txt', etc.)
        if '.' in dokLink:
            extension = dokLink.rsplit('.', 1)[1].lower()  # Get the file extension in lowercase
            if extension in ['pdf']:
                #print("file handler specific file type (pdf)")
                folder_icon_path = pdf_file  # PDF file icon
            elif extension in ['asice']:
                #print("file handler specific file type (asice)")
                folder_icon_path = digidoc_file  # Digidoc file icon
            else:
                # Handle other file extensions or set a default file icon
                #print("file handler other file types")
                #folder_icon_path = universal_file
                test_icon = icon_paths.icon_show_on_map()
                folder_icon_path = test_icon
        else:
            #print("file handler else type")
            folder_icon_path = open_folder

        return folder_icon_path
