# Decrypt password-protected PDF in Python.
# 
# Requirements:
# pip install pikepdf

from pikepdf import Pdf
import pikepdf
import os


def decrypt_Pikepdf(input_path, output_path, password):
  with Pdf.open(input_path, password=password) as pdf:
    pdf.save(output_path)
  

if __name__ == '__main__':
  # example usage:
  # decrypt_Pikepdf('payslip_02_2020.pdf', 'payslip.pdf', 'GP58i714')
  dirName = 'cracked'
  # Create directory to store uncrypted PDF
  try:
    os.mkdir(dirName)
    print('Directory', dirName, 'created')
  except FileExistsError: 
    print('Directory', dirName, 'already exists')
  
  # Getting PDF files
  while True:
    direc = input('Name of directory with PDF files: ')
    if len(direc) < 1 : direc = '.'
    if not os.path.exists(direc):
      print('No directory named', direc)
      continue
    break
  arr_pdf = [x for x in os.listdir(direc) if x.endswith('.pdf')]
  print(len(arr_pdf), 'PDF files found.')
  pwd = input('Please insert password: ')
  if len(pwd) < 1 : pwd = 'GP58i714'
  countnon = 0
  countyes = 0
  for file in arr_pdf:
    # print(dirName+'/'+file)
    try: 
      decrypt_Pikepdf(direc+'/'+file, dirName+'/'+file, pwd)
      print(direc+'/'+file, 'decrypted in', dirName+'/'+file)
      countyes = countyes + 1
    except pikepdf._qpdf.PasswordError:
      print(direc+'/'+file, '- Password incorrect')
      countnon = countnon + 1
    

  print(countyes, 'files decrypted and', countnon, 'files non decrypted')