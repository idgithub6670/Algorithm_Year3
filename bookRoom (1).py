import re
import time
def find_num(str):
    # ค้นหาตัวเลขใน String แล้วเก็บค่า
    result = re.findall("[0-9]+", str) 
    
    return result # ส่งกลับข้อมูลตัวเลขที่เก็บไว้

def sortArr(arr, meeting, n): # Cube Sort Algorithm
    sort_value_time = []
    pos_meeting = []

    arr = [(int(arr[i]) ** 3, int(arr[i]), i+1) for i in range(int(meeting[0]))]

    arr.sort()

    for i in range(n):
        sort_value_time.append(arr[i][1])
        pos_meeting.append(arr[i][2])

    return sort_value_time, pos_meeting

def meeting_room_reservations02(sort_value_time, pos_meeting, max): #Greedy Algorithms

    sum = 0
    result = []
    value_time_sum = []

    while len(sort_value_time) != 0:
        sum = sum + sort_value_time[0]
        result.append([sort_value_time[0],pos_meeting[0]])
        value_time_sum.append(sum)
        
        if sum + sort_value_time[0] > max:
            
            sort_value_time.pop(0)
            pos_meeting.pop(0)
            
            return result
        sort_value_time.pop(0)
        pos_meeting.pop(0)
    return 

def write_output_file(result_info, sort_value_time):
    #print(result_info)
    for i in range(len(result_info)):
        flie2.write("%s:"% (i+1))
        #print(i) 
        for j in result_info[i]:
            #print(j)
            flie2.write("%s(%s)"% (j[1],j[0]))
        flie2.write("\n")
    flie2.write("0:"%sort_value_time)
    flie2.write("%s "%sort_value_time)
        
    


flie1 = open("Midterm Project/meeting_room03.txt","r") # อ่านไฟล์
flie2 = open("Midterm Project/room_reservation.txt","w") # เขียนไฟล์

room = find_num(flie1.readline()) # จำนวนห้องประชุม
meeting = find_num(flie1.readline()) # จำนวนการประชุม
value_time = find_num(flie1.readline())   # เวลาการใช้ห้องประชุม
max = int(input("Enter the longest meeting time(hrs) : "))
print("Room :",room[0])
print("Meeting : ", meeting[0])

start = time.time() # เริ่มนับเวลา
sort_value_time, pos_meeting = sortArr(value_time, meeting, len(value_time))
result_info = []
for x in range(int(room[0])):
    result_info.append(meeting_room_reservations02(sort_value_time, pos_meeting, max))
end = time.time()   # จบการนับเวลา

print("empty set",sort_value_time)
write_output_file(result_info, sort_value_time)

print("%f" %((end - start) / 1000))
flie1.close()
flie2.close()