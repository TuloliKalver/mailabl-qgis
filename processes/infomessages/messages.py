from PyQt5.QtWidgets import QMessageBox, QPushButton


def SaveCadastrals_Success_message(self):
    # Create a QMessageBox with custom buttons
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    text = (
        "Valitud kihid on edaspidi automaatselt seadistatud.\n"
        "Seadistuste muutmiseks pead teostama muudatused <b>Sätetes</b>."
    )
    msg_box.setText(text)
    msg_box.setWindowTitle("Hoiatus")
    msg_box.addButton(QPushButton("Edasi"), QMessageBox.AcceptRole)
    msg_box.addButton(QPushButton("Tühista"), QMessageBox.RejectRole)

    # Show the QMessageBox and handle the result
    result = msg_box.exec_()

    if result == QMessageBox.AcceptRole:
        QMessageBox.information(self, "Info", "Andmed edukalt salvestatud.")
        # Call the function to continue the process
    elif result == QMessageBox.RejectRole:
        # Cancel button was pressed, stop the process
        QMessageBox.information(self, "Info", "Andmeid ei salvestatud.")

        # Stop the process or perform necessary actions


#shp failiga seotud hoiatused

def SHP_layer_not_present():
    # Create a QMessageBox with custom buttons
    text = (
        "Lae õige fail! SHP_KATASTRIÜKSUS.SHP\n"
        "Uued andmed saad Maa-ametist, kasutades Sätete nenüüst valikut 'Maa-ametisse'"
    )
     # Show the QMessageBox and handle the result
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText(text)
    msg_box.setWindowTitle("Hoiatus")
    msg_box.exec_()

#Kui eraldi faili võimalik lahednada siis asenda import fail koodiga
def SHP_file_loading_time():
    # Create a QMessageBox with custom buttons
    text = (
        "Eesti katastriandmete maht on pea xxx tuhat!\n"
        "Seega võib andmete laadimine võtta omajagu aega\n!"
        "Samal ajal ei ole soovitulik kasutada arvutis muid tegevusi\n"
        "Millal sa viimati kohvi jõid\n"
        "Mine tee üks kohvi ja tule 2min pärast tagasi\n"
        "Sesnis aga vajuta OK nuppu"
    )
     # Show the QMessageBox and handle the result
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText(text)
    msg_box.setWindowTitle("Hoiatus")
    msg_box.exec_()