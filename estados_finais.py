#program
text='0”begin”1(1(1(1"float"5|1"int"6|1"string"7|1"void"8|1"bool"9|1"char"10)4(4(4"Identifier"13[13"["15"Integer-Number"16"]"17]14)12{18","19(19"Identifier"21[21"["23"Integer-Number"24"]"25]22)20}18)11|1(1"float"27|1"int"28|1"string"29|1"void"30|1"bool"31|1"char"32)26"["33"]"34(34(34"Identifier"37[37"["39"Integer-Number"40"]"41]38)36{42","42(42"Identifier"44[44"["46"Integer-Number"47"]"48]45)43}49)35";"50)3|1(1(1"float"53|1"int"54|1"string"55|1"void"56|1"bool"57|1"char"58)52"Function"59"("60[6(6(6(6"float"65|6"int"66|6"string"67|6"void"68|6"bool"69|6"char"70)64(64(64"Identifier"73[73"["75"Integer-Number"76"]"77]74)72{78","78(78"Identifier"80[8"["82"Integer-Number"83"]"84]81)79}85)71)63{86";"86(86(86"float"89|86"int"90|86"string"91|86"void"92|86"bool"93|86"char"94)88(88(88"Identifier"97[97"["99"Integer-Number"100"]"101]98)96{102","102(102"Identifier"104[104"["106"Integer-Number"107"]"108]105)103}109)95)87}110)62]61")"111statement112)51)2{113";"113(113(113(113"float"117|113"int"118|113"string"119|113"void"120|113"bool"121|113"char"122)116(116(116"Identifier"125[125"["127"Integer-Number"128"]"129]126)124{130","130(13"Identifier"132[132"["134"Integer-Number"135"]"136]133)131}137)123|113(113"float"139|113"int"140|113"string"141|113"void"142|113"bool"143|113"char"144)138"["145"]"146(146(146"Identifier"149[149"["151"Integer-Number"152"]"153]150)148{154","154(154"Identifier"156[156"["158"Integer-Number"159"]"160]157)155}161)147";"162)115|113(113(113"float"165|113"int"166|113"string"167|113"void"168|113"bool"169|113"char"170)164"Function"171"("172[172(172(172(172"float"177|172"int"178|172"string"179|172"void"180|172"bool"181|172"char"182)176(176(176"Identifier"185[185"["187"Integer-Number"188"]"189]186)184{190","190(19"Identifier"192[192"["194"Integer-Number"195"]"196]193)191}197)183)175{198";"198(198(198"float"201|198"int"202|198"string"203|198"void"204|198"bool"205|198"char"206)200(2(2"Identifier"209[209"["211"Integer-Number"212"]"213]210)208{214","214(214"Identifier"216[216"["218"Integer-Number"219"]"220]217)215}221)207)199}222)174]173")"223statement224)163)114}225“end”226'

#statement
#text='0(0[0(0{4(4"Identifier"6[6"["8"Integer-Number"9"]"10]7)5"="11}4(4(4(4{15"!"15}16(16(16(16(16{21"-"21}22factor23)20{24(24"*"25|24"/"26)24(24{28"-"28}29factor30)27}31)19{32(32"+"33|32"-"34)32(32(32{37"-"37}38factor39)36{40(4"*"41|4"/"42)40(4{44"-"44}45factor46)43}47)35}48)18[18(18"="51|18">"52|18">="53|18"<"54|18"<="55|18"=="56|18"!="57|18"#"58)50(5(5(5{62"-"62}63factor64)61{65(65"*"66|65"/"67)65(65{69"-"69}70factor71)68}72)60{73(73"+"74|73"-"75)73(73(73{78"-"78}79factor80)77{81(81"*"82|81"/"83)81(81{85"-"85}86factor87)84}88)76}89)59]49)17)14{90"&"90(9{92"!"92}93(93(93(93(93{98"-"98}99factor100)97{101(101"*"102|101"/"103)101(101{105"-"105}106factor107)104}108)96{109(109"+"110|109"-"111)109(109(109{114"-"114}115factor116)113{117(117"*"118|117"/"119)117(117{121"-"121}122factor123)120}124)112}125)95[95(95"="128|95">"129|95">="130|95"<"131|95"<="132|95"=="133|95"!="134|95"#"135)127(127(127(127{139"-"139}140factor141)138{142(142"*"143|142"/"144)142(142{146"-"146}147factor148)145}149)137{150(15"+"151|15"-"152)150(15(15{155"-"155}156factor157)154{158(158"*"159|158"/"160)158(158{162"-"162}163factor164)161}165)153}166)136]126)94)91}167)13{168"|"168(168(168{171"!"171}172(172(172(172(172{177"-"177}178factor179)176{180(18"*"181|18"/"182)180(18{184"-"184}185factor186)183}187)175{188(188"+"189|188"-"190)188(188(188{193"-"193}194factor195)192{196(196"*"197|196"/"198)196(196{200"-"200}201factor202)199}203)191}204)174[174(174"="207|174">"208|174">="209|174"<"210|174"<="211|174"=="212|174"!="213|174"#"214)206(206(206(206{218"-"218}219factor220)217{221(221"*"222|221"/"223)221(221{225"-"225}226factor227)224}228)216{229(229"+"230|229"-"231)229(229(229{234"-"234}235factor236)233{237(237"*"238|237"/"239)237(237{241"-"241}242factor243)240}244)232}245)215]205)173)170{246"&"246(246{248"!"248}249(249(249(249(249{254"-"254}255factor256)253{257(257"*"258|257"/"259)257(257{261"-"261}262factor263)260}264)252{265(265"+"266|265"-"267)265(265(265{270"-"270}271factor272)269{273(273"*"274|273"/"275)273(273{277"-"277}278factor279)276}280)268}281)251[251(251"="284|251">"285|251">="286|251"<"287|251"<="288|251"=="289|251"!="290|251"#"291)283(283(283(283{295"-"295}296factor297)294{298(298"*"299|298"/"300)298(298{302"-"302}303factor304)301}305)293{306(306"+"307|306"-"308)306(306(306{311"-"311}312factor313)310{314(314"*"315|314"/"316)314(314{318"-"318}319factor320)317}321)309}322)292]282)250)247}323)169}324)12)3]2";"325)1|0(0"{"327{328(328(328"float"330|328"int"331|328"string"332|328"void"333|328"bool"334|328"char"335)329(329(329"Identifier"338[338"["340"Integer-Number"341"]"342]339)337{343","343(343"Identifier"345[345"["347"Integer-Number"348"]"349]346)344}350)336|328(328"float"352|328"int"353|328"string"354|328"void"355|328"bool"356|328"char"357)351"["358"]"359(359(359"Identifier"362[362"["364"Integer-Number"365"]"366]363)361{367","367(367"Identifier"369[369"["371"Integer-Number"372"]"373]370)368}374)360";"375)328}376{377statement377}378"}"379)326|0(0"if"381"("382(382{384(384"Identifier"385[385"["387"Integer-Number"388"]"389]386)384"="390}391(391(391(391{395"!"395}396(396(396(396(396{401"-"401}402factor403)400{404(404"*"405|404"/"406)404(404{408"-"408}409factor410)407}411)399{412(412"+"413|412"-"414)412(412(412{417"-"417}418factor419)416{420(42"*"421|42"/"422)420(42{424"-"424}425factor426)423}427)415}428)398[398(398"="431|398">"432|398">="433|398"<"434|398"<="435|398"=="436|398"!="437|398"#"438)430(43(43(43{442"-"442}443factor444)441{445(445"*"446|445"/"447)445(445{449"-"449}450factor451)448}452)440{453(453"+"454|453"-"455)453(453(453{458"-"458}459factor460)457{461(461"*"462|461"/"463)461(461{465"-"465}466factor467)464}468)456}469)439]429)397)394{470"&"470(47{472"!"472}473(473(473(473(473{478"-"478}479factor480)477{481(481"*"482|481"/"483)481(481{485"-"485}486factor487)484}488)476{489(489"+"490|489"-"491)489(489(489{494"-"494}495factor496)493{497(497"*"498|497"/"499)497(497{501"-"501}502factor503)500}504)492}505)475[475(475"="508|475">"509|475">="510|475"<"511|475"<="512|475"=="513|475"!="514|475"#"515)507(507(507(507{519"-"519}520factor521)518{522(522"*"523|522"/"524)522(522{526"-"526}527factor528)525}529)517{530(53"+"531|53"-"532)530(53(53{535"-"535}536factor537)534{538(538"*"539|538"/"540)538(538{542"-"542}543factor544)541}545)533}546)516]506)474)471}547)393{548"|"548(548(548{551"!"551}552(552(552(552(552{557"-"557}558factor559)556{560(56"*"561|56"/"562)560(56{564"-"564}565factor566)563}567)555{568(568"+"569|568"-"570)568(568(568{573"-"573}574factor575)572{576(576"*"577|576"/"578)576(576{580"-"580}581factor582)579}583)571}584)554[554(554"="587|554">"588|554">="589|554"<"590|554"<="591|554"=="592|554"!="593|554"#"594)586(586(586(586{598"-"598}599factor600)597{601(601"*"602|601"/"603)601(601{605"-"605}606factor607)604}608)596{609(609"+"610|609"-"611)609(609(609{614"-"614}615factor616)613{617(617"*"618|617"/"619)617(617{621"-"621}622factor623)620}624)612}625)595]585)553)550{626"&"626(626{628"!"628}629(629(629(629(629{634"-"634}635factor636)633{637(637"*"638|637"/"639)637(637{641"-"641}642factor643)640}644)632{645(645"+"646|645"-"647)645(645(645{650"-"650}651factor652)649{653(653"*"654|653"/"655)653(653{657"-"657}658factor659)656}660)648}661)631[631(631"="664|631">"665|631">="666|631"<"667|631"<="668|631"=="669|631"!="670|631"#"671)663(663(663(663{675"-"675}676factor677)674{678(678"*"679|678"/"680)678(678{682"-"682}683factor684)681}685)673{686(686"+"687|686"-"688)686(686(686{691"-"691}692factor693)690{694(694"*"695|694"/"696)694(694{698"-"698}699factor700)697}701)689}702)672]662)630)627}703)549}704)392)383")"705statement706[706"else"708statement709]707)380|0(0"while"711"("712(712{714(714"Identifier"715[715"["717"Integer-Number"718"]"719]716)714"="720}721(721(721(721{725"!"725}726(726(726(726(726{731"-"731}732factor733)730{734(734"*"735|734"/"736)734(734{738"-"738}739factor740)737}741)729{742(742"+"743|742"-"744)742(742(742{747"-"747}748factor749)746{750(75"*"751|75"/"752)750(75{754"-"754}755factor756)753}757)745}758)728[728(728"="761|728">"762|728">="763|728"<"764|728"<="765|728"=="766|728"!="767|728"#"768)760(76(76(76{772"-"772}773factor774)771{775(775"*"776|775"/"777)775(775{779"-"779}780factor781)778}782)770{783(783"+"784|783"-"785)783(783(783{788"-"788}789factor790)787{791(791"*"792|791"/"793)791(791{795"-"795}796factor797)794}798)786}799)769]759)727)724{800"&"800(8{802"!"802}803(803(803(803(803{808"-"808}809factor810)807{811(811"*"812|811"/"813)811(811{815"-"815}816factor817)814}818)806{819(819"+"820|819"-"821)819(819(819{824"-"824}825factor826)823{827(827"*"828|827"/"829)827(827{831"-"831}832factor833)830}834)822}835)805[805(805"="838|805">"839|805">="840|805"<"841|805"<="842|805"=="843|805"!="844|805"#"845)837(837(837(837{849"-"849}850factor851)848{852(852"*"853|852"/"854)852(852{856"-"856}857factor858)855}859)847{860(86"+"861|86"-"862)860(86(86{865"-"865}866factor867)864{868(868"*"869|868"/"870)868(868{872"-"872}873factor874)871}875)863}876)846]836)804)801}877)723{878"|"878(878(878{881"!"881}882(882(882(882(882{887"-"887}888factor889)886{890(89"*"891|89"/"892)890(89{894"-"894}895factor896)893}897)885{898(898"+"899|898"-"900)898(898(898{903"-"903}904factor905)902{906(906"*"907|906"/"908)906(906{910"-"910}911factor912)909}913)901}914)884[884(884"="917|884">"918|884">="919|884"<"920|884"<="921|884"=="922|884"!="923|884"#"924)916(916(916(916{928"-"928}929factor930)927{931(931"*"932|931"/"933)931(931{935"-"935}936factor937)934}938)926{939(939"+"940|939"-"941)939(939(939{944"-"944}945factor946)943{947(947"*"948|947"/"949)947(947{951"-"951}952factor953)950}954)942}955)925]915)883)880{956"&"956(956{958"!"958}959(959(959(959(959{964"-"964}965factor966)963{967(967"*"968|967"/"969)967(967{971"-"971}972factor973)970}974)962{975(975"+"976|975"-"977)975(975(975{980"-"980}981factor982)979{983(983"*"984|983"/"985)983(983{987"-"987}988factor989)986}990)978}991)961[961(961"="994|961">"995|961">="996|961"<"997|961"<="998|961"=="999|961"!="1000|961"#"1001)993(993(993(993{1005"-"1005}1006factor1007)1004{1008(1008"*"1009|1008"/"1010)1008(1008{1012"-"1012}1013factor1014)1011}1015)1003{1016(1016"+"1017|1016"-"1018)1016(1016(1016{1021"-"1021}1022factor1023)1020{1024(1024"*"1025|1024"/"1026)1024(1024{1028"-"1028}1029factor1030)1027}1031)1019}1032)1002]992)960)957}1033)879}1034)722)713")"1035statement1036)710|0(0"return"1038[1038(1038{1041(1041"Identifier"1042[1042"["1044"Integer-Number"1045"]"1046]1043)1041"="1047}1048(1048(1048(1048{1052"!"1052}1053(1053(1053(1053(1053{1058"-"1058}1059factor1060)1057{1061(1061"*"1062|1061"/"1063)1061(1061{1065"-"1065}1066factor1067)1064}1068)1056{1069(1069"+"1070|1069"-"1071)1069(1069(1069{1074"-"1074}1075factor1076)1073{1077(1077"*"1078|1077"/"1079)1077(1077{1081"-"1081}1082factor1083)1080}1084)1072}1085)1055[1055(1055"="1088|1055">"1089|1055">="1090|1055"<"1091|1055"<="1092|1055"=="1093|1055"!="1094|1055"#"1095)1087(1087(1087(1087{1099"-"1099}1100factor1101)1098{1102(1102"*"1103|1102"/"1104)1102(1102{1106"-"1106}1107factor1108)1105}1109)1097{1110(111"+"1111|111"-"1112)1110(111(111{1115"-"1115}1116factor1117)1114{1118(1118"*"1119|1118"/"1120)1118(1118{1122"-"1122}1123factor1124)1121}1125)1113}1126)1096]1086)1054)1051{1127"&"1127(1127{1129"!"1129}1130(113(113(113(113{1135"-"1135}1136factor1137)1134{1138(1138"*"1139|1138"/"1140)1138(1138{1142"-"1142}1143factor1144)1141}1145)1133{1146(1146"+"1147|1146"-"1148)1146(1146(1146{1151"-"1151}1152factor1153)1150{1154(1154"*"1155|1154"/"1156)1154(1154{1158"-"1158}1159factor1160)1157}1161)1149}1162)1132[1132(1132"="1165|1132">"1166|1132">="1167|1132"<"1168|1132"<="1169|1132"=="1170|1132"!="1171|1132"#"1172)1164(1164(1164(1164{1176"-"1176}1177factor1178)1175{1179(1179"*"1180|1179"/"1181)1179(1179{1183"-"1183}1184factor1185)1182}1186)1174{1187(1187"+"1188|1187"-"1189)1187(1187(1187{1192"-"1192}1193factor1194)1191{1195(1195"*"1196|1195"/"1197)1195(1195{1199"-"1199}1200factor1201)1198}1202)1190}1203)1173]1163)1131)1128}1204)1050{1205"|"1205(1205(1205{1208"!"1208}1209(1209(1209(1209(1209{1214"-"1214}1215factor1216)1213{1217(1217"*"1218|1217"/"1219)1217(1217{1221"-"1221}1222factor1223)1220}1224)1212{1225(1225"+"1226|1225"-"1227)1225(1225(1225{1230"-"1230}1231factor1232)1229{1233(1233"*"1234|1233"/"1235)1233(1233{1237"-"1237}1238factor1239)1236}1240)1228}1241)1211[1211(1211"="1244|1211">"1245|1211">="1246|1211"<"1247|1211"<="1248|1211"=="1249|1211"!="1250|1211"#"1251)1243(1243(1243(1243{1255"-"1255}1256factor1257)1254{1258(1258"*"1259|1258"/"1260)1258(1258{1262"-"1262}1263factor1264)1261}1265)1253{1266(1266"+"1267|1266"-"1268)1266(1266(1266{1271"-"1271}1272factor1273)1270{1274(1274"*"1275|1274"/"1276)1274(1274{1278"-"1278}1279factor1280)1277}1281)1269}1282)1252]1242)1210)1207{1283"&"1283(1283{1285"!"1285}1286(1286(1286(1286(1286{1291"-"1291}1292factor1293)1290{1294(1294"*"1295|1294"/"1296)1294(1294{1298"-"1298}1299factor1300)1297}1301)1289{1302(1302"+"1303|1302"-"1304)1302(1302(1302{1307"-"1307}1308factor1309)1306{1310(131"*"1311|131"/"1312)1310(131{1314"-"1314}1315factor1316)1313}1317)1305}1318)1288[1288(1288"="1321|1288">"1322|1288">="1323|1288"<"1324|1288"<="1325|1288"=="1326|1288"!="1327|1288"#"1328)1320(132(132(132{1332"-"1332}1333factor1334)1331{1335(1335"*"1336|1335"/"1337)1335(1335{1339"-"1339}1340factor1341)1338}1342)1330{1343(1343"+"1344|1343"-"1345)1343(1343(1343{1348"-"1348}1349factor1350)1347{1351(1351"*"1352|1351"/"1353)1351(1351{1355"-"1355}1356factor1357)1354}1358)1346}1359)1329]1319)1287)1284}1360)1206}1361)1049)1040]1039";"1362)1037|0(0"break"1364";"1365)1363'

#factor
#text='0"("1(1{3(3"Identifier"5[5"["7"Integer-Number"8"]"9]6)4"="10}3(3(3(3{14"!"14}15(15(15(15(15{20"-"20}21factor22)19{23(23"*"24|23"/"25)23(23{27"-"27}28factor29)26}30)18{31(31"+"32|31"-"33)31(31(31{36"-"36}37factor38)35{39(39"*"40|39"/"41)39(39{43"-"43}44factor45)42}46)34}47)17[17(17"="50|17">"51|17">="52|17"<"53|17"<="54|17"=="55|17"!="56|17"#"57)49(49(49(49{61"-"61}62factor63)60{64(64"*"65|64"/"66)64(64{68"-"68}69factor70)67}71)59{72(72"+"73|72"-"74)72(72(72{77"-"77}78factor79)76{80(8"*"81|8"/"82)80(8{84"-"84}85factor86)83}87)75}88)58]48)16)13{89"&"89(89{91"!"91}92(92(92(92(92{97"-"97}98factor99)96{100(1"*"101|1"/"102)100(1{104"-"104}105factor106)103}107)95{108(108"+"109|108"-"110)108(108(108{113"-"113}114factor115)112{116(116"*"117|116"/"118)116(116{120"-"120}121factor122)119}123)111}124)94[94(94"="127|94">"128|94">="129|94"<"130|94"<="131|94"=="132|94"!="133|94"#"134)126(126(126(126{138"-"138}139factor140)137{141(141"*"142|141"/"143)141(141{145"-"145}146factor147)144}148)136{149(149"+"150|149"-"151)149(149(149{154"-"154}155factor156)153{157(157"*"158|157"/"159)157(157{161"-"161}162factor163)160}164)152}165)135]125)93)90}166)12{167"|"167(167(167{170"!"170}171(171(171(171(171{176"-"176}177factor178)175{179(179"*"180|179"/"181)179(179{183"-"183}184factor185)182}186)174{187(187"+"188|187"-"189)187(187(187{192"-"192}193factor194)191{195(195"*"196|195"/"197)195(195{199"-"199}200factor201)198}202)190}203)173[173(173"="206|173">"207|173">="208|173"<"209|173"<="210|173"=="211|173"!="212|173"#"213)205(205(205(205{217"-"217}218factor219)216{220(22"*"221|22"/"222)220(22{224"-"224}225factor226)223}227)215{228(228"+"229|228"-"230)228(228(228{233"-"233}234factor235)232{236(236"*"237|236"/"238)236(236{240"-"240}241factor242)239}243)231}244)214]204)172)169{245"&"245(245{247"!"247}248(248(248(248(248{253"-"253}254factor255)252{256(256"*"257|256"/"258)256(256{260"-"260}261factor262)259}263)251{264(264"+"265|264"-"266)264(264(264{269"-"269}270factor271)268{272(272"*"273|272"/"274)272(272{276"-"276}277factor278)275}279)267}280)250[25(25"="283|25">"284|25">="285|25"<"286|25"<="287|25"=="288|25"!="289|25"#"290)282(282(282(282{294"-"294}295factor296)293{297(297"*"298|297"/"299)297(297{301"-"301}302factor303)300}304)292{305(305"+"306|305"-"307)305(305(305{310"-"310}311factor312)309{313(313"*"314|313"/"315)313(313{317"-"317}318factor319)316}320)308}321)291]281)249)246}322)168}323)11)2")"324|0(0"Identifier"326[326"["328"Integer-Number"329"]"330]327)325|0(0"Function"332"("333[333factor335{336","336(336{338(338"Identifier"339[339"["341"Integer-Number"342"]"343]340)338"="344}345(345(345(345{349"!"349}350(35(35(35(35{355"-"355}356factor357)354{358(358"*"359|358"/"360)358(358{362"-"362}363factor364)361}365)353{366(366"+"367|366"-"368)366(366(366{371"-"371}372factor373)370{374(374"*"375|374"/"376)374(374{378"-"378}379factor380)377}381)369}382)352[352(352"="385|352">"386|352">="387|352"<"388|352"<="389|352"=="390|352"!="391|352"#"392)384(384(384(384{396"-"396}397factor398)395{399(399"*"400|399"/"401)399(399{403"-"403}404factor405)402}406)394{407(407"+"408|407"-"409)407(407(407{412"-"412}413factor414)411{415(415"*"416|415"/"417)415(415{419"-"419}420factor421)418}422)410}423)393]383)351)348{424"&"424(424{426"!"426}427(427(427(427(427{432"-"432}433factor434)431{435(435"*"436|435"/"437)435(435{439"-"439}440factor441)438}442)430{443(443"+"444|443"-"445)443(443(443{448"-"448}449factor450)447{451(451"*"452|451"/"453)451(451{455"-"455}456factor457)454}458)446}459)429[429(429"="462|429">"463|429">="464|429"<"465|429"<="466|429"=="467|429"!="468|429"#"469)461(461(461(461{473"-"473}474factor475)472{476(476"*"477|476"/"478)476(476{480"-"480}481factor482)479}483)471{484(484"+"485|484"-"486)484(484(484{489"-"489}490factor491)488{492(492"*"493|492"/"494)492(492{496"-"496}497factor498)495}499)487}500)470]460)428)425}501)347{502"|"502(502(502{505"!"505}506(506(506(506(506{511"-"511}512factor513)510{514(514"*"515|514"/"516)514(514{518"-"518}519factor520)517}521)509{522(522"+"523|522"-"524)522(522(522{527"-"527}528factor529)526{530(53"*"531|53"/"532)530(53{534"-"534}535factor536)533}537)525}538)508[508(508"="541|508">"542|508">="543|508"<"544|508"<="545|508"=="546|508"!="547|508"#"548)540(54(54(54{552"-"552}553factor554)551{555(555"*"556|555"/"557)555(555{559"-"559}560factor561)558}562)550{563(563"+"564|563"-"565)563(563(563{568"-"568}569factor570)567{571(571"*"572|571"/"573)571(571{575"-"575}576factor577)574}578)566}579)549]539)507)504{580"&"580(58{582"!"582}583(583(583(583(583{588"-"588}589factor590)587{591(591"*"592|591"/"593)591(591{595"-"595}596factor597)594}598)586{599(599"+"600|599"-"601)599(599(599{604"-"604}605factor606)603{607(607"*"608|607"/"609)607(607{611"-"611}612factor613)610}614)602}615)585[585(585"="618|585">"619|585">="620|585"<"621|585"<="622|585"=="623|585"!="624|585"#"625)617(617(617(617{629"-"629}630factor631)628{632(632"*"633|632"/"634)632(632{636"-"636}637factor638)635}639)627{640(64"+"641|64"-"642)640(64(64{645"-"645}646factor647)644{648(648"*"649|648"/"650)648(648{652"-"652}653factor654)651}655)643}656)626]616)584)581}657)503}658)346)337}659]334")"660)331|0(0(0"Integer-Number"663|0"Float-Number"664)662|0(0"Constant-String"666|0"Character"667)665|0"true"668|0"false"669)661'

#example
#text='0"a"1"b"2(2"c"4|2A5(5"a"7|5"b"8)6)3|0[0"a"10|0"b"11]9{12"b"13"c"14|12A15|12B16}12"("16'

text = text.replace(" ","")
fin = []
state =0 
i=0 
opend = 0   
while i < len(text):
    if (text[i] == '{' or text[i]=='[' or text[i]=='(') and text[i+1] !='"':
        opend+=1
    if (text[i] == '}' or text[i]==']' or text[i]==')') and text[i+1] !='"':
        opend-=1
    if text[i]=='|' and text[i+1] !='"' and opend==0:
        aux=i
        while(ord(text[aux-1]) >= ord('0') and ord(text[aux-1])<= ord('9')):
            aux-=1
        while(ord(text[aux]) >= ord('0') and ord(text[aux])<= ord('9')):
            state*=10
            state+=ord(text[aux]) - ord('0')
            aux+=1    
        fin.append(state)
        state=0    
    i+=1

aux=len(text)-1
count = 0
while(ord(text[aux-1]) >= ord('0') and ord(text[aux-1])<= ord('9')):
    aux-=1
    count+=1
aux=len(text)-count-1
while(aux!=len(text)):
    state*=10
    state+=ord(text[aux]) - ord('0')
    aux+=1    
fin.append(state)

f = open("estados_program.txt", "a")
f.write('Inicial: 0\n\n')
f.write('Finais: ')
f.write(str(fin))
f.close()