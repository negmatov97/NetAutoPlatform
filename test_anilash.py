import models.SNR_modul
import models.TL_modul

command = models.TL_modul.show.sh_vlan()
print(command)

if "231" in command:
    models.TL_modul.config.c_vl()
elif "232" in command:
    models.SNR_modul.config.c_vl()
else:
    "Qurilma modellari bilan xatolik yuz berdi!!!"
