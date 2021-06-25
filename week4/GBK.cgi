$gbkhtml="/html/wp109b/week4/gbk.html";
$gbkurl="https://shaoan901226.github.io/wp109b/week4/gbk.html";
read(STDIN, $temp, $ENV{'CONTENT_LENGTH'});
@pairs=split(/&/,$temp);
foreach $item(@pairs)  {
  ($key,$content)=split (/=/,$item,2);
  $content=~tr/+/ /;
  $content=~ s/%(..)/pack("c",hex($1))/ge;
  $OLS3{$key}=$content;
}
$name=$OLS3{'name'};
$comment=$OLS3{'comment'};
$comment=~ s/\cM\n/<br>\n/g;
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=gmtime(time+8*60*60);
if (length ($min) == 1) {$min = '0'.$min;}
if (length ($sec) == 1) {$sec = '0'.$sec;}
$mon+=1;
$date="$mon/$mday/$year, $hour:$min:$sec";
open(FHD, "$gbkhtml") || die "Content-type: text/html\n\n 開啟檔案錯誤!\n";
@all=<FHD>;
close(FHD);
open(FHD, ">$gbkhtml") || die "Content-type: text/html\n\n 開啟檔案錯誤!\n";
foreach $line(@all) {

   
if ($line =~ /<!--ols3-->/)  
 {
    print FHD "<!--ols3-->\n";
    print FHD "姓名: $name [時間: $date]<p>$comment<hr size=1>\n";
 } 
 else 
   {
   print FHD $line;
   }
 }
 close(FHD);
print "Content-type: text/html\n\n";
print "<html><head>\n";
print "<META HTTP-EQUIV=REFRESH CONTENT=\"3;URL=$gbkurl\">\n";
print "<title>Thanks!</title></head>\n";
print "<body bgcolor=white><center>\n";
print "謝謝您的留言!\n";
print "</center></body></html>\n";
