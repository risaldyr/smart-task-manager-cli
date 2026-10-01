import json

def load_task():
     try:
          with open("tasks.json", "r") as file:
               tasks = json.load(file)
               return tasks
     except FileNotFoundError:
          return []
     except json.JSONDecodeError:
          return []


tasks = load_task()


def input_task_id():
     while True:
          try:
               return int(input("\n Masukan ID = "))
          except ValueError:
               print("Data Harus Angka")
               
          
def show_menu():
    print("=" * 35)
    print("      SMART TASK MANAGER")
    print("=" * 35)
    print("1. Tambah Task")
    print("2. Lihat Task")
    print("3. Update Status")
    print("4. Hapus Task")
    print("5. Keluar")
    
def save_task():
     with open("tasks.json", "w") as file:
          json.dump(tasks, file, indent= 4)
     

def add_task(): 
     title = input("\nMasukan Task : ").strip()
     if not title: 
          print("\nTidak Boleh Kosong")
     else:
          found = False
                    
          for task_new in tasks:
               if task_new["title"].lower() == title.lower():
                    found = True
                    break
          
          if found:
               print("Data Sudah ada")
          else:
               id_list = []
               for task_new in tasks:
                    id_list.append(task_new["id"])
               
               max_id = 0
               
               if id_list:
                    max_id = max(id_list)
                    
               
               task = {
                         "id": max_id + 1,
                         "title": title,
                         "status": "pending"
                         }
               tasks.append(task)
               save_task()
               print("data berhasil dimasukan")
               print(tasks)


def show_task():
     if not tasks:
          print("data belum ada")
     else:
           print("=" * 35)
           print("      List Data")
           print("=" * 35)
           for task in tasks:
                print(f"ID : {task['id']} | Task : {task['title']} | Status : {task['status']}")


def update_task():
     if not tasks:
          print("\nData Tidak Ada")
     else:
          found = False
          task_id = input_task_id()
          for task in tasks:
               if task["id"] == task_id:
                    print("\nBerhasil ditemukan")
                    found = True
                    while True:
                         task["status"] = input("\nSilahkan Update Status = ").strip()
                         if task["status"] == "":
                              print("Data Tidak Boleh Kosong")
                         else:
                              save_task()
                              print(f"Status sudah diupdate Menjadi {task["status"]}")
                              break
          if not found:
               print("Data tidak ditemukan")          
               

def delete_task():
     option = ""

     if not tasks:
          print("\nData Tidak Ada")
     else:
          found = False
          task_id = input_task_id()
                    
          for i in tasks:
               if i["id"] == task_id:
                    print("\nBerhasil ditemukan")
                    found = True
                    while True:
                         option= input(f"Yakin mau menghapus data dengan judul {i['title']} (Y/n)?").strip().lower()
                         if option == "y" :
                              tasks.remove(i)
                              save_task()
                              print("\nData Sudah dihapus")
                              break
                         elif option == "n":
                              print("\nData tidak jadi dihapus")
                              break
                         elif option == "":
                              print("\nTidak boleh kosong silahkan isi kembali")
                         else:
                              print("\nIsi hanya Y:(setuju) n:(tidak setuju), Silahkan ulang kembali")
          if not found:
               print("\nData Tidak ditemukan")

def main():

    running = True


    while running:
          
        show_menu()

        choice = input("Pilih Menu = ")

        if choice == "1":
             add_task()

        elif choice == "2":
             show_task()

        elif choice == "3":
             update_task()

        elif choice == "4":
             delete_task()
        
        elif choice == "5":
             print("Program Selesai")
             running = False

        else:
             print("Menu Tidak Tersedia")

if __name__ == "__main__":
        main()

