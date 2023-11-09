import re

def find_num(str):
    # ค้นหาตัวเลขใน String แล้วเก็บค่า
    result = re.findall("[0-9]+", str) 
    return result # ส่งกลับข้อมูลตัวเลขที่เก็บไว้

def sortArr(arr, meeting, n): # Cube Sort Algorithm
    sort_time = []
    pos_meeting = []
    count = 0
    # Make a list of tuples in
    # the form(cube of (num), num)
    arr = [(int(arr[i]) ** 3, int(arr[i]), i+1) for i in range(int(meeting[0]))]
     
    # Sort the array according to
    # the their respective cubes
    arr.sort()
    
    for i in range(n):
        sort_time.append(arr[i][1])
        pos_meeting.append(arr[i][2])
    print(sort_time)
    print(pos_meeting)
    return sort_time, pos_meeting

def meeting_room_reservations02(sort_time, pos_meeting, max): #Greedy Algorithms

    sum = 0
    result = []
    time_sum = []

    while len(sort_time) != 0:
        sum = sum + sort_time[0]
        result.append([sort_time[0],pos_meeting[0]])
        time_sum.append(sum)
        
        if sum + sort_time[0] > max:
            
            sort_time.pop(0)
            pos_meeting.pop(0)
            
            return result
        sort_time.pop(0)
        pos_meeting.pop(0)
    return 

def write_output_file(result_info, time):

    for i in range(len(result_info)):
        flie2.write("%s:"% (i+1))
        print(i)
        for j in result_info[i]:
            print(j)
            flie2.write("%s(%s)"% (j[1],j[0]))
        flie2.write("\n")
        
def write_output_file02(result_info, time):

    for i in range(len(result_info)):
        flie2.write("%s:%s"% ((i+1),result_info[i[0]]))
        #for j in result_info[i]:



flie1 = open("Midterm Project/meeting_room.txt","r") # อ่านไฟล์
flie2 = open("Midterm Project/room_reservation.txt","w") # เขียนไฟล์

room = find_num(flie1.readline()) # จำนวนห้องประชุม
meeting = find_num(flie1.readline()) # จำนวนการประชุม
time = find_num(flie1.readline())   # เวลาการใช้ห้องประชุม

max = int(input("Enter the longest meeting time(hrs) : "))

#print(room)
#print(meeting)
#print(time)
#merge_sort(time) 

sort_time, pos_meeting = sortArr(time, meeting, len(time))

#print(sort_time)
#print(time)

result_info = []
for x in range(int(room[0])):
    #print(meeting_room_reservations02(sort_time, pos_meeting, max))
    result_info.append(meeting_room_reservations02(sort_time, pos_meeting, max))


print(result_info)
print("empty set",sort_time)
write_output_file(result_info, time)


flie1.close()
flie2.close()