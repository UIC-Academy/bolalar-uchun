# Merchant API payment flow


1. User "sotib olish" tugmasini bosadi.
2. Unga maxsus link generatsiya qilib beriladi (generate_payment_link)
3. User linkka kiradi, to'lovni amalga oshiradi (to'lash tugmasini bosadi)
4. Paylov sizning CALLBACK_URL ingizga "transaction.check" requestini jo'natadi.
5. Siz "transaction.check" ni handle qilasiz va response qaytarasiz. Agar response successful bo'lsa
6. Paylov sizning CALLBACK_URL ingizga "transaction.perform" requestini jo'natadi
7. Siz "transaction.perform" ni handle qilasiz va tranzaksiyani lokalingizda successful qilib saqlab qo'yasiz.
8. User home pagega redirect qilinadi.



if res == 1:
return yes
if res == 0:
return no


l = {1: yes, 0: no}