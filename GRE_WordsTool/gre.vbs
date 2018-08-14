Public Sub swap (a,b)
c = a: a = b: b = c
End Sub
Dim a()
Randomize
Set spell = CreateObject("sapi.spvoice") 
currentfolder = createobject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
Set   ExcelApp  =  CreateObject("Excel.Application")      
Set   ExcelBook =  ExcelApp.Workbooks.open(currentfolder+"/gre.xlsx")


flag0=MsgBox("选择刷词词库 红宝(选择是)3000(选择否)", vbYesNo, "提示")
if flag0=vbYes then
Set   ExcelSheet   =   ExcelBook.Worksheets("新红宝2012")
      ExcelSheet.Select
elseif flag0=vbNo then
Set   ExcelSheet   =   ExcelBook.Worksheets("3000")
      ExcelSheet.Select
end if

ExcelApp.Visible = True

 

flag=MsgBox("是否开启单词发音功能？", vbYesNo, "提示")

if flag0=vbYes then

i = InputBox("输入起始序号:")
if i<2 then i=2
j = InputBox("请输入终止序号（最大为6497）:")
if j>6497 then j=6497

elseif flag0=vbNo then

i = InputBox("输入起始序号:")
if i<2 then i=2
j = InputBox("请输入终止序号（最大为3105）:")
if j>3105 then j=3105

end if
num=j-i+1
msgbox ("您选择的单词数目为:"&num)
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
     re=msgbox(ExcelSheet.Range("A"&a(m)).Value&" "&ExcelSheet.Range("B"&a(m)).Value&ExcelSheet.Range("C"&a(m)).Value,vbYesNo,"加油！O(∩_∩)O~")

      if re=vbNo then
	      ExcelSheet.Cells(a(m),4).value = ExcelSheet.Cells(a(m),4).value+1 
       end if
   ExcelSheet.Cells(a(m),5).value = ExcelSheet.Cells(a(m),5).value+1 
Next 


r=MsgBox("退出并关闭gre.xlsx？", vbYesNo, "提示")
If r = vbYes Then
ExcelBook.Close (True) 
ExcelApp.Quit 
Set ExcelApp = Nothing 
Set spell = Nothing
end If

