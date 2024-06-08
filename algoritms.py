import threading
import time


from datetime import datetime

file = open('info.txt','r+',encoding = "utf-8")

class Apartment:
    def __init__(self, number):
        self.number = number


class CallInit:
    def __init__(self, apartmentNumber, callTime, doorOpened):
        self.apartmentNumber = apartmentNumber
        self.callTime = callTime
        self.doorOpened = doorOpened


def timer_function(timeout, call):
    time.sleep(timeout)
    if end == 0:
        print(f"Час вийшов. Відсутня відповідь. \n{goodbye}")
        response = None
       


class ApartmentSorting:
    @staticmethod
    def bubble_sort(apartments):
        n = len(apartments)
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, n):
                if apartments[i - 1].number < apartments[i].number:
                    apartments[i - 1], apartments[i] = apartments[i], apartments[i - 1]
                    swapped = True


class ApartmentSearch:
    @staticmethod
    def binary_search(apartments, target):
        left = 0
        right = len(apartments) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if apartments[mid].number == target:
                return mid
            elif apartments[mid].number > target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == "__main__":
    apartments = [
        Apartment(41),
        Apartment(42),
        Apartment(43),
        Apartment(44),
        Apartment(45),
        Apartment(46),
        Apartment(47),
        Apartment(48),
        Apartment(49),
        Apartment(50),
        Apartment(51),
        Apartment(52),
        Apartment(53),
        Apartment(54),
        Apartment(55),
        Apartment(56),
        Apartment(57),
        Apartment(58),
        Apartment(59),
        Apartment(60),
    ]

    ApartmentSorting.bubble_sort(apartments)

   
    
    name = input("Вітаємо! Введіть будь ласка Ваше ім'я : ")
    print(f"{name}, оберіть будь ласка дію, яку хочете виконати \n1. Зателефонувати до іншої квартири \n2. Перевірити історію викликів \n")
    option = input()


    if option == "1":
        print("Оберіть квартиру, до якої хочете зателефонувати")
        print("Список квартир:")
        for i, apartment in enumerate(apartments, start=1):
            print(apartment.number, end=" ")
            if i % 4 == 0:
                print()

        data_info = datetime.now()
        #file.write(str(data_info))

        goodbye = "Дякую за користування нашим сервісом! До побачення! :)"
        target_apartment = int(input("Введіть номер квартири \n"))
        file.write("Номер квартири : ")
        file.write(str(target_apartment))
        file.write("\n Дата та час : ")
        file.write(str(data_info))
        file.close()

        apartment_index = ApartmentSearch.binary_search(apartments, target_apartment)
        end = 0

        if apartment_index != -1:
            call = CallInit(apartments[apartment_index].number, time.time(), False)
            print(f"Дзвінок до квартири {call.apartmentNumber}. Очікуємо відповіді...")

          

            timeout_thread = threading.Thread(target=timer_function, args=(12, call))
            timeout_thread.start()
            response = input("Відчинити двері? (Так/Ні): \n")
        
            while True:
                if response.lower() == "так":
                    call.doorOpened = True
                    print(f"Двері відкриті. \n{goodbye}")
                    end += 1
                    break
                
                elif response.lower() == "ні":
                    print(f"Двері заблоковано. \n{goodbye}")
                    end += 1
                    break
        
                timeout_thread.join()
        else:
            print("Квартиру не знайдено.")
    if option == "2":
        print("Інформація про останній виклик :\n",file.read())
        
