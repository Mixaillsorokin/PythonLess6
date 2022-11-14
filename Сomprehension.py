# N = int(input('N :'))
# numlist=[]
# for i in range(1,N):
#     if (N % i==0):
#         if(i % i==0)and(i%1==0):
#             numlist.append(i)
# print(f'Простые множетели N-го числа => {numlist}')

numlist = [i  for i in range(1,int(input('N :'))) if N % i==0 if(i % i==0)and(i%1==0)]
print(f'Простые множетели N-го числа => {numlist}')