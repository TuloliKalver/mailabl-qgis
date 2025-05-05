from .settings import Filepaths, IconsByName

icon_paths = Filepaths()

open_folder = Filepaths.get_icon(IconsByName().icon_folder)   #ava kaust ikoon - uus vaja
digidoc_file = Filepaths.get_icon(IconsByName().icon_digi_doc_name)
word_file = Filepaths.get_icon(IconsByName().icon_word)
exel_file = Filepaths.get_icon(IconsByName().icon_xls)
universal_file = Filepaths.get_icon(IconsByName().icon_unknown)  #Üldine fail millelle sisu hetkel ei anna
pdf_file = Filepaths.get_icon(IconsByName().icon_pdf)    #pdf failid 
no_file = Filepaths.get_icon(IconsByName().no_files)
autocad = Filepaths.get_icon(IconsByName().icon_autocad)
dgn = Filepaths.get_icon(IconsByName().icon_dgn)
text_file = Filepaths.get_icon(IconsByName().icon_text)
image_file = Filepaths.get_icon(IconsByName().icon_image)
video_file = Filepaths.get_icon(IconsByName().icon_video)
archive_file = Filepaths.get_icon(IconsByName().icon_archive)
html_file = Filepaths.get_icon(IconsByName().icon_html)
gis_file = Filepaths.get_icon(IconsByName().icon_gis)
edit_data = Filepaths.get_icon(IconsByName().edit_data)




class iconHandler:
    @staticmethod
    def set_document_icon_based_on_item(dokLink):

        # Check for a file extension (e.g., '.pdf', '.txt', etc.)
        if '.' in dokLink:
            extension = dokLink.rsplit('.', 1)[1].lower()  # Get the file extension in lowercase
            if extension in ['pdf']:
                #print("file handler specific file type (pdf)")
                folder_icon_path = pdf_file  # PDF file icon
            elif extension in ['asice', 'bdoc', 'ddoc']:
                #print("file handler specific file type (asice)")
                folder_icon_path = digidoc_file  # Digidoc file icon
            elif extension in ['xlsx', 'xls', 'ods']:
                folder_icon_path = exel_file
            elif extension in ['docx', 'doc', 'odt']:
                folder_icon_path = word_file
            elif extension in ['dwg', 'dxf', 'dwt']:                
                folder_icon_path = autocad
            elif extension in ['dgn']:
                folder_icon_path = dgn
            elif extension in ['txt', 'rtf', 'csv', 'log', 'ini']:
                folder_icon_path = text_file
            elif extension in [ 'html']:
                folder_icon_path = html_file
            elif extension in ['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv']:
                folder_icon_path = video_file
            elif extension in ['zip', 'rar', '7z', 'tar', 'gz']:
                folder_icon_path = archive_file
            elif extension in ['svg', 'png', 'jpg', 'jpeg', 'bmp', 'gif', 'tif', 'tiff']:
                folder_icon_path = image_file
            elif extension in ['shp', 'kml', 'kmz', 'gml', 'geojson']:
                folder_icon_path = gis_file
            else:
                folder_icon_path = universal_file
        else:
            folder_icon_path = open_folder

        return folder_icon_path


    @staticmethod
    def set_no_file_icon():
        folder_icon_path = no_file
        return folder_icon_path
    @staticmethod
    def edit_data():
        open_folder = edit_data
        return open_folder
    
