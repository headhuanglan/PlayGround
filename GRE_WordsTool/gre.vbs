Public Sub swap (a,b)
c = a: a = b: b = c
End Sub
Dim a()
Randomize
Set spell = CreateObject("sapi.spvoice") 
currentfolder = createobject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
Set   ExcelApp  =  CreateObject("Excel.Application")      
Set   ExcelBook =  ExcelApp.Workbooks.open(currentfolder+"/gre.xlsx")


flag0=MsgBox("ѡ��ˢ�ʴʿ� �챦(ѡ����)3000(ѡ���)", vbYesNo, "��ʾ")
if flag0=vbYes then
Set   ExcelSheet   =   ExcelBook.Worksheets("�º챦2012")
      ExcelSheet.Select
elseif flag0=vbNo then
Set   ExcelSheet   =   ExcelBook.Worksheets("3000")
      ExcelSheet.Select
end if

ExcelApp.Visible = True

 

flag=MsgBox("�Ƿ������ʷ������ܣ�", vbYesNo, "��ʾ")

if flag0=vbYes then

i = InputBox("������ʼ���:")
if i<2 then i=2
j = InputBox("��������ֹ��ţ����Ϊ6497��:")
if j>6497 then j=6497

elseif flag0=vbNo then

i = InputBox("������ʼ���:")
if i<2 then i=2
j = InputBox("��������ֹ��ţ����Ϊ3105��:")
if j>3105 then j=3105

end if
num=j-i+1
msgbox ("��ѡ��ĵ�����ĿΪ:"&num)
ReDim a(num) 
For k = 1 To num
  a(k) = i + k - 1
Next 
For s = 1 To num
  Call swap(a(s), a(Int(Rnd() * num) + 1))
Next 
For m = 1 To num
     if flag=vbYes then
         spell.speak ExcelSheet.Range("A"&a(m)).Value
      end if
     re=msgbox(ExcelSheet.Range("A"&a(m)).Value&" "&ExcelSheet.Range("B"&a(m)).Value&ExcelSheet.Range("C"&a(m)).Value,vbYesNo,"���ͣ�O(��_��)O~")

      if re=vbNo then
	      ExcelSheet.Cells(a(m),4).value = ExcelSheet.Cells(a(m),4).value+1 
       end if
   ExcelSheet.Cells(a(m),5).value = ExcelSheet.Cells(a(m),5).value+1 
Next 


r=MsgBox("�˳����ر�gre.xlsx��", vbYesNo, "��ʾ")
If r = vbYes Then
ExcelBook.Close (True) 
ExcelApp.Quit 
Set ExcelApp = Nothing 
Set spell = Nothing
end If

