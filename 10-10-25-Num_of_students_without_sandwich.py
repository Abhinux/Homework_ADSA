class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while (len(students)!=0):
            l=len(students)
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                i=1
                while(i<l):
                    if students[i]==sandwiches[0]:
                        break
                    i+=1
                if i==l:
                    break
                for j in range(i):
                    to_add=students.pop(0)
                    students.append(to_add)
                
        return len(students)