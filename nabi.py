from __future__ import annotations

import sys
import webbrowser
from urllib.parse import quote_plus

import pygame


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 760
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("THE GREAT JOURNEY — 17 Kitab")
clock = pygame.time.Clock()

BG = (16, 18, 29)
PANEL = (29, 34, 51)
PANEL2 = (43, 49, 70)
WHITE = (245, 244, 238)
MUTED = (178, 184, 200)
GOLD = (231, 194, 91)
GREEN = (116, 192, 145)

FONT = pygame.font.SysFont("segoeui", 21)
SMALL = pygame.font.SysFont("segoeui", 17)
BIG = pygame.font.SysFont("segoeui", 29, bold=True)
TITLE = pygame.font.SysFont("segoeui", 43, bold=True)

BOOKS = [
    ("Yesaya", "Yesaya bin Amos", "sekitar abad ke-8 SM, kitab mencakup masa yang lebih luas", "Yehuda, terutama Yerusalem", "Yesaya, Ahas, Hizkia, Sennakerib, serafim, umat Yehuda"),
    ("Yeremia", "Yeremia bin Hilkia", "sekitar 627–586 SM, dengan materi sesudahnya", "Yehuda dan Yerusalem", "Yeremia, Barukh, Yosia, Yoyakim, Zedekia, Nebukadnezar, Hananya"),
    ("Ratapan", "Yeremia bin Hilkia", "sesudah jatuhnya Yerusalem, abad ke-6 SM", "Yerusalem", "Penyair/umat yang meratap, Yerusalem sebagai personifikasi, umat Yehuda"),
    ("Yehezkiel", "Yehezkiel bin Buzi", "sekitar 593–571 SM", "Komunitas buangan di Babel", "Yehezkiel, para tua-tua, umat buangan, Gog, Israel/Yehuda"),
    ("Daniel", "Daniel", "latar pembuangan Babel; penanggalan komposisi diperdebatkan", "Babel dan lingkungan kekaisaran", "Daniel, Sadrakh, Mesakh, Abednego, Nebukadnezar, Belsyazar, Darius, Gabriel"),
    ("Hosea", "Hosea bin Beeri", "abad ke-8 SM", "Kerajaan Israel/Efraim", "Hosea, Gomer, anak-anak mereka, raja-raja Israel, umat"),
    ("Yoel", "Yoel bin Petuel", "tanggal tidak pasti", "Yehuda dan Yerusalem", "Yoel, imam, umat Yehuda, bangsa-bangsa"),
    ("Amos", "Amos dari Tekoa", "sekitar pertengahan abad ke-8 SM", "Israel utara", "Amos, Amazia, Yerobeam II, orang miskin, umat Israel"),
    ("Obaja", "Obaja", "tanggal tidak pasti; sering dikaitkan dengan masa sesudah kejatuhan Yerusalem", "Edom dan Yerusalem", "Obaja, Edom, Yehuda/Yerusalem"),
    ("Yunus", "Yunus bin Amitai", "tanggal kitab tidak pasti; tokoh ditempatkan pada masa Yerobeam II", "Niniwe, laut, dan Israel", "Yunus, pelaut, raja Niniwe, penduduk Niniwe, Tuhan"),
    ("Mikha", "Mikha dari Moresyet", "sekitar 740–700 SM", "Yehuda dan Israel", "Mikha, pemimpin, imam, nabi, orang kaya, umat"),
    ("Nahum", "Nahum dari Elkos", "sebelum jatuhnya Niniwe sekitar 612 SM", "Niniwe/Asyur dan Yehuda", "Nahum, Niniwe/Asyur, Yehuda"),
    ("Habakuk", "Habakuk", "akhir abad ke-7 SM", "Yehuda dan konteks kebangkitan Babel", "Habakuk, Tuhan, orang Kasdim/Babel"),
    ("Zefanya", "Zefanya bin Kusyi", "masa Yosia, sekitar 640–609 SM", "Yehuda dan Yerusalem", "Zefanya, Yosia, umat Yehuda, bangsa-bangsa, sisa umat"),
    ("Hagai", "Hagai", "520 SM", "Yerusalem setelah pembuangan", "Hagai, Zerubabel, Yosua imam besar, umat"),
    ("Zakharia", "Zakharia bin Berekhya bin Ido", "sekitar 520–518 SM untuk bagian awal; bagian akhir diperdebatkan", "Yerusalem setelah pembuangan", "Zakharia, Zerubabel, Yosua, malaikat, penunggang kuda, dua pohon zaitun"),
    ("Maleakhi", "Maleakhi", "sekitar abad ke-5 SM", "Yehuda dan Yerusalem", "Maleakhi, imam, umat, utusan, Elia yang dinubuatkan"),
]

STORIES = {
"Yesaya":[
("Panggilan Yesaya — Yerusalem", "Pada masa Uzia, Yotam, Ahas, dan Hizkia, Yesaya bin Amos dipanggil Tuhan di Bait Allah. Ia melihat kemuliaan Tuhan dan serafim yang menyatakan kekudusan-Nya. Ketika Yesaya menyadari kenajisan dirinya dan bangsanya, Tuhan menyucikannya lalu mengutusnya. Sejak saat itu, Yesaya berdiri di tengah Yehuda sebagai nabi yang membawa teguran sekaligus pengharapan."),
("Yehuda yang sakit dari dalam", "Yesaya berbicara kepada Yehuda yang tetap beribadah tetapi hidupnya dipenuhi ketidakadilan. Ia menegur para pemimpin dan umat karena ibadah tidak boleh dipisahkan dari pertobatan dan kepedulian kepada yang lemah. Pesannya jelas: Tuhan melihat kehidupan umat, bukan hanya kegiatan keagamaannya."),
("Ahas dan ancaman Aram", "Ketika Ahas menjadi raja Yehuda, Rezin raja Aram dan Pekah bin Remalya raja Israel menyerang Yehuda. Yesaya datang menemui Ahas dan meminta agar ia tetap percaya kepada Tuhan. Ahas justru mencari bantuan Asyur. Di tengah krisis itu, Yesaya menyampaikan tanda Imanuel: Tuhan menyertai umat-Nya."),
("Hizkia dan Asyur", "Hizkia, anak Ahas, menjadi raja Yehuda dan membawa persoalan Asyur kepada Tuhan. Sennakerib, raja Asyur, mengancam Yerusalem melalui utusannya. Hizkia berdoa dan Yesaya menyampaikan firman Tuhan. Yerusalem tidak diselamatkan karena kekuatan politik Yehuda, melainkan karena Tuhan bertindak."),
("Dari Babel menuju penghiburan", "Sesudah itu Yesaya memperingatkan Hizkia bahwa harta Yehuda suatu hari akan dibawa ke Babel. Namun kitab tidak berhenti pada pembuangan. Suara Tuhan kemudian berubah menjadi penghiburan bagi umat yang akan mengalami kehancuran. Tuhan tetap menjadi gembala yang membawa umat-Nya pulang."),
("Raja yang dijanjikan", "Di tengah kegelapan, Yesaya berbicara tentang terang dan seorang Raja yang memerintah dengan keadilan dan damai. Gambaran tentang tunas dari Isai dan kerajaan yang benar membuat harapan Yehuda tidak berhenti pada keadaan politik saat itu. Dalam pembacaan Kristen, bagian-bagian ini juga dibaca dalam terang pengharapan Mesias."),
("Hamba Tuhan", "Yesaya memperkenalkan sosok Hamba Tuhan yang taat dan menderita. Dalam Yesaya 52–53, penderitaan Hamba digambarkan berkaitan dengan dosa dan pemulihan banyak orang. Identitas Hamba ditafsirkan beragam dalam studi Alkitab, sementara tradisi Kristen membacanya secara kuat dalam kaitannya dengan Kristus."),
("Langit baru dan bumi baru", "Perjalanan Yesaya bergerak menuju pemulihan. Tuhan mengundang umat untuk mencari-Nya dan menutup kitab dengan gambaran langit baru dan bumi baru. Setelah teguran, krisis, pembuangan, dan penderitaan, harapan terakhir tetap berada pada Tuhan yang menciptakan dan memulihkan."),
],
"Yeremia":[
("Yeremia dipanggil", "Yeremia bin Hilkia berasal dari Anatot. Pada masa Yosia, Tuhan memanggilnya sejak muda untuk berbicara kepada Yehuda. Barukh kemudian menjadi juru tulis dan pendampingnya. Panggilan Yeremia bukan perjalanan menuju kenyamanan, tetapi tugas untuk mencabut dan merobohkan sekaligus membangun dan menanam."),
("Yosia dan Yehuda", "Yosia menjadi raja Yehuda dan melakukan pembaruan keagamaan. Namun Yeremia melihat bahwa perubahan lahiriah belum otomatis mengubah hati bangsa. Ia memperingatkan bahwa Yehuda telah meninggalkan Tuhan, sumber air hidup, dan mencari keamanan pada berhala serta kekuatan manusia."),
("Pintu Bait Allah", "Yeremia berdiri di pintu Bait Allah dan berbicara kepada orang-orang yang merasa aman karena Bait Tuhan ada di tengah mereka. Ia mengingatkan bahwa tempat suci tidak dapat menjadi alasan untuk terus melakukan kejahatan. Tuhan menghendaki pertobatan, keadilan, dan ketaatan."),
("Yoyakim dan gulungan kitab", "Pada masa Yoyakim, Barukh menuliskan perkataan Yeremia dalam sebuah gulungan. Ketika gulungan itu dibacakan kepada raja, Yoyakim membakarnya bagian demi bagian. Tindakan itu tidak menghentikan firman Tuhan; Yeremia dan Barukh kembali menuliskannya."),
("Zedekia dan Yerusalem", "Zedekia menjadi raja terakhir Yehuda sebelum Yerusalem jatuh. Ia berkali-kali mendengar Yeremia tetapi berada di tengah tekanan politik dan ketakutan. Nebukadnezar, raja Babel, akhirnya mengepung Yerusalem. Peringatan Yeremia menjadi kenyataan dan kota itu jatuh."),
("Surat kepada orang buangan", "Setelah pembuangan dimulai, Yeremia tidak menyuruh umat hidup tanpa harapan. Ia menulis kepada mereka agar membangun kehidupan di Babel sambil menantikan waktu Tuhan. Janji tentang masa depan dan damai harus dibaca dalam konteks umat yang sedang berada dalam pembuangan, bukan sebagai jalan pintas menuju keadaan langsung nyaman."),
("Perjanjian baru", "Di tengah berita penghakiman, Tuhan memberikan janji yang lebih dalam: perjanjian baru. Hukum Tuhan akan ditaruh dalam batin dan ditulis dalam hati. Jadi pemulihan bukan hanya kembalinya sebuah bangsa ke tanahnya, tetapi pembaruan hubungan manusia dengan Tuhan."),
("Sisa harapan", "Yeremia berakhir di tengah reruntuhan dan pergantian kekuasaan. Namun kisah itu tidak menghapus kesetiaan Tuhan. Kehancuran Yerusalem menjadi akhir sebuah zaman, sekaligus membuka pertanyaan besar tentang bagaimana Tuhan akan memulihkan umat yang telah dihukum karena ketidaksetiaan mereka."),
],
"Ratapan":[
("Yerusalem menangis", "Ratapan membuka perjalanan dengan Yerusalem yang dahulu ramai tetapi kini seperti seorang janda. Penyair menggambarkan kota, umat, dan penderitaan setelah kehancuran. Tidak ada usaha untuk memperindah luka; kesedihan disebut apa adanya di hadapan Tuhan."),
("Dosa dan penghakiman", "Di balik kehancuran itu, Ratapan mengakui bahwa umat Yehuda telah berdosa dan karena itu mengalami penghakiman. Kota yang dahulu menjadi pusat kehidupan kini menyaksikan kelaparan, kehilangan, dan pembuangan. Ratapan memandang tragedi dengan serius tanpa menghapus tanggung jawab manusia."),
("Kasih setia di tengah gelap", "Di pasal ketiga, suara penyair berhenti sejenak untuk mengingat sesuatu yang tidak berubah: kasih setia Tuhan. Keadaan Yerusalem belum pulih, tetapi harapan dapat tumbuh karena rahmat Tuhan tidak berakhir. Di sinilah ratapan berubah menjadi penantian."),
("Doa pemulihan", "Pada akhirnya, umat membawa seluruh luka mereka kembali kepada Tuhan. Mereka meminta agar Tuhan memulihkan mereka. Ratapan tidak memberi akhir yang mudah; kitab justru menunjukkan bahwa iman dapat membawa kesedihan yang nyata langsung kepada Tuhan."),
],
"Yehezkiel":[
("Kemuliaan Tuhan di Babel", "Yehezkiel bin Buzi adalah seorang imam yang berada di tengah orang-orang Yehuda yang dibuang ke Babel. Di sana ia melihat penglihatan tentang kemuliaan Tuhan. Ini menjadi pesan penting: jatuhnya Yerusalem tidak berarti Tuhan kehilangan kuasa atau meninggalkan sejarah umat-Nya."),
("Yehezkiel sebagai penjaga", "Tuhan menetapkan Yehezkiel sebagai penjaga bagi kaum Israel. Tugasnya adalah mendengar firman Tuhan dan memperingatkan umat. Ia tidak dipanggil untuk mengatakan hal yang paling menyenangkan, tetapi untuk menyampaikan tanggung jawab dan konsekuensi di hadapan Tuhan."),
("Para tua-tua dan dosa Yerusalem", "Para tua-tua Israel datang kepada Yehezkiel untuk mencari jawaban. Namun penglihatan Yehezkiel menunjukkan bahwa masalah umat jauh lebih dalam daripada keadaan politik. Penyembahan berhala dan pemberontakan telah merusak kehidupan mereka bahkan di sekitar Bait Allah."),
("Kemuliaan meninggalkan kota", "Yehezkiel melihat kemuliaan Tuhan bergerak menjauh dari Yerusalem. Penglihatan itu menunjukkan bahwa keberadaan Bait Allah tidak boleh diperlakukan sebagai jaminan otomatis ketika umat terus memberontak. Penghakiman datang, tetapi Tuhan tetap menguasai apa yang terjadi."),
("Hati baru dan roh baru", "Sesudah berbicara tentang penghakiman, Tuhan menjanjikan sesuatu yang lebih dalam kepada umat. Ia akan memberikan hati yang baru dan roh yang baru. Pemulihan berarti Tuhan sendiri mengubah batin umat sehingga mereka dapat hidup menurut kehendak-Nya."),
("Lembah tulang kering", "Yehezkiel dibawa ke sebuah lembah yang penuh tulang kering. Gambaran itu melukiskan keadaan yang tampak tanpa harapan. Ketika Yehezkiel menyampaikan firman Tuhan, tulang-tulang itu mendapat kehidupan kembali. Penglihatan ini menunjuk pada pemulihan Israel oleh kuasa Tuhan."),
("Tuhan hadir kembali", "Bagian akhir kitab membawa Yehezkiel kepada penglihatan tentang pemulihan, tanah, umat, dan Bait Allah. Nama kota itu menjadi penutup yang kuat: Tuhan hadir di sana. Setelah pembuangan dan kehancuran, kehadiran Tuhan kembali menjadi pusat harapan."),
],
"Daniel":[
("Daniel dibawa ke Babel", "Daniel dan tiga sahabatnya—Sadrakh, Mesakh, dan Abednego—dibawa dari Yehuda ke lingkungan kerajaan Babel. Mereka harus belajar dalam budaya baru tanpa kehilangan kesetiaan kepada Tuhan. Daniel menetapkan hati untuk tidak menajiskan dirinya dengan santapan raja."),
("Nebukadnezar dan mimpi", "Nebukadnezar, raja Babel, mengalami mimpi yang tidak dapat dijelaskan para ahli hikmatnya. Daniel berdoa bersama sahabat-sahabatnya dan Tuhan menyatakan rahasia itu. Daniel menegaskan bahwa hikmat dan pengetahuan bukan berasal dari dirinya, melainkan dari Tuhan."),
("Patung emas", "Nebukadnezar mendirikan patung emas dan menuntut semua orang menyembahnya. Sadrakh, Mesakh, dan Abednego menolak. Mereka tetap setia kepada Tuhan meskipun konsekuensinya berat. Kisah itu menempatkan kesetiaan kepada Tuhan di atas keselamatan pribadi."),
("Kesombongan Nebukadnezar", "Nebukadnezar kembali berhadapan dengan pesan Tuhan melalui mimpi. Daniel menjelaskan bahwa kesombongan raja akan direndahkan. Pada akhirnya Nebukadnezar mengakui bahwa Yang Mahatinggi berkuasa atas kerajaan manusia. Raja besar pun tidak berada di atas Tuhan."),
("Belsyazar dan tulisan di dinding", "Belsyazar mengadakan pesta kerajaan dan memakai perkakas dari Bait Allah. Tulisan misterius muncul di dinding. Daniel dipanggil untuk menjelaskannya dan menyatakan bahwa kerajaan Belsyazar telah ditimbang. Malam itu menjadi titik balik kekuasaan Babel."),
("Daniel dan Darius", "Pada masa Darius, Daniel tetap dikenal karena kesetiaannya. Para pejabat yang iri mencari alasan untuk menjatuhkannya dan membuat larangan berdoa. Daniel tetap berdoa kepada Tuhan. Ia kemudian dilemparkan ke gua singa, tetapi Tuhan menyertainya."),
("Empat binatang dan Anak Manusia", "Dalam penglihatan Daniel, kerajaan-kerajaan manusia digambarkan seperti binatang yang datang dan berlalu. Lalu Daniel melihat sosok seperti Anak Manusia menerima kuasa dan kerajaan yang kekal. Penglihatan itu mengangkat pandangan dari kerajaan yang sementara kepada pemerintahan yang tidak berakhir."),
("Masa depan dan kebangkitan", "Penglihatan terakhir Daniel berbicara tentang masa kesesakan, pembebasan umat, dan kebangkitan. Beberapa rincian penglihatan tetap misterius bagi Daniel sendiri. Kitab berakhir dengan panggilan untuk tetap setia dan menantikan penggenapan yang Tuhan pegang."),
],
"Hosea":[
("Hosea dan Gomer", "Hosea bin Beeri dipanggil menjadi nabi bagi Israel. Tuhan memakai kehidupan rumah tangga Hosea dengan Gomer sebagai tanda profetis tentang hubungan-Nya dengan Israel. Ketidaksetiaan dalam rumah tangga menjadi gambaran tentang ketidaksetiaan umat terhadap Tuhan."),
("Israel mengejar yang lain", "Israel terus mencari Baal, kekuatan politik, dan keamanan di luar Tuhan. Hosea menjelaskan bahwa masalah mereka bukan sekadar salah memilih strategi, tetapi meninggalkan hubungan perjanjian dengan Allah. Karena itu teguran Hosea terasa seperti teguran terhadap hati yang berpaling."),
("Anak-anak sebagai tanda", "Anak-anak Hosea menjadi bagian dari pesan melalui nama-nama mereka. Nama-nama itu menyampaikan keadaan hubungan Tuhan dengan Israel dan konsekuensi dosa mereka. Dengan cara ini, kehidupan nabi dan keluarganya menjadi bagian dari bahasa nubuat."),
("Kasih yang memanggil pulang", "Walaupun penghakiman dinyatakan, Tuhan tidak berhenti memanggil Israel. Ia berbicara tentang belas kasih dan kasih setia yang tidak sama dengan sikap manusia. Hosea memperlihatkan bahwa pertobatan bukan sekadar takut dihukum, tetapi kembali kepada Pribadi yang mengasihi."),
("Sembuh dan kembali", "Pada akhir kitab, Hosea memanggil Israel untuk kembali kepada Tuhan. Pemulihan digambarkan seperti kesembuhan dan pertumbuhan. Perjalanan kitab bergerak dari pengkhianatan menuju undangan pulang: Tuhan tetap membuka jalan bagi umat yang mau kembali."),
],
"Yoel":[
("Hari ketika belalang datang", "Yoel bin Petuel menggambarkan bencana belalang yang menghancurkan hasil tanah. Para imam dan umat menghadapi krisis yang nyata. Yoel tidak hanya meminta mereka menghitung kerugian, tetapi mengajak mereka melihat bahwa krisis itu seharusnya membawa mereka kembali kepada Tuhan."),
("Kembali dengan segenap hati", "Yoel memanggil umat Yehuda untuk berpuasa, menangis, dan berbalik kepada Tuhan. Para imam diminta mengumpulkan umat untuk berseru kepada Tuhan. Dasarnya bukan sekadar ketakutan, melainkan pengenalan bahwa Tuhan pengasih dan penyayang."),
("Tuhan memulihkan", "Setelah panggilan pertobatan, Yoel menyampaikan janji pemulihan. Tuhan akan memulihkan tahun-tahun yang dimakan belalang dan kembali menjadi tempat perlindungan bagi umat-Nya. Krisis tidak menjadi kata terakhir."),
("Roh dicurahkan", "Janji pemulihan mencapai puncak ketika Tuhan berjanji mencurahkan Roh-Nya atas manusia. Anak-anak, orang tua, laki-laki dan perempuan sama-sama disebut. Yoel memperluas harapan dari pemulihan tanah menuju karya Roh Tuhan di tengah umat."),
("Bangsa-bangsa di hadapan Tuhan", "Kitab kemudian melihat bangsa-bangsa yang berhadapan dengan penghakiman Tuhan. Tuhan bertindak sebagai pembela umat-Nya sekaligus hakim atas kejahatan. Akhirnya, Yehuda digambarkan sebagai tempat di mana Tuhan tinggal bersama umat-Nya."),
],
"Amos":[
("Amos dari Tekoa", "Amos berasal dari Tekoa dan bekerja sebagai peternak serta pemungut buah ara hutan. Ia bukan nabi istana. Tuhan mengambilnya dari pekerjaannya dan mengutusnya kepada Israel utara pada masa Yerobeam II."),
("Bangsa-bangsa dan Israel", "Amos mulai dengan menyampaikan penghakiman terhadap bangsa-bangsa di sekitar Israel. Namun arah pesannya kemudian berbalik kepada Israel sendiri. Menjadi umat pilihan tidak berarti bebas dari pertanggungjawaban; justru pengetahuan tentang Tuhan membuat tanggung jawab mereka semakin serius."),
("Orang miskin ditindas", "Amos melihat masyarakat yang makmur tetapi tidak adil. Orang miskin dijual, hukum diputarbalikkan, dan orang lemah tidak mendapat perlindungan. Karena itu Amos menolak agama yang berjalan berdampingan dengan penindasan."),
("Amazia melawan Amos", "Amazia, imam di Betel, menyuruh Amos pergi dan kembali bernubuat di Yehuda. Amos menjawab bahwa ia bukan mencari jabatan sebagai nabi; Tuhanlah yang mengambilnya dari pekerjaannya dan mengutusnya. Konflik itu menunjukkan betapa seriusnya pesan Amos bagi pusat keagamaan Israel."),
("Lima penglihatan dan harapan", "Amos menerima penglihatan tentang belalang, api, tali sipat, keranjang buah musim kemarau, dan Tuhan yang berdiri di dekat mezbah. Semua itu bergerak menuju penghakiman Israel. Namun kitab berakhir dengan janji bahwa pondok Daud yang roboh akan dibangun kembali."),
],
"Obaja":[
("Obaja berbicara kepada Edom", "Obaja menyampaikan pesan Tuhan tentang Edom. Edom berkaitan erat dengan Israel melalui Esau dan Yakub, tetapi hubungan saudara itu tidak mencegah konflik. Obaja menyoroti kesombongan Edom yang merasa aman di tempat tinggi."),
("Ketika Yerusalem jatuh", "Saat Yerusalem mengalami bencana, Edom tidak berdiri sebagai saudara yang menolong. Mereka bersukacita, memandang malapetaka Yehuda, dan mengambil keuntungan. Obaja menilai tindakan itu sebagai kesalahan yang akan diperhitungkan Tuhan."),
("Hari Tuhan", "Obaja memperluas pesan dari Edom kepada prinsip Hari Tuhan: apa yang dilakukan akan kembali kepada pelakunya. Kesombongan bangsa-bangsa tidak menjadi akhir sejarah. Pada penutupnya, kerajaan menjadi milik Tuhan dan Sion menerima harapan pemulihan."),
],
"Yunus":[
("Yunus dipanggil ke Niniwe", "Yunus bin Amitai menerima perintah Tuhan untuk pergi ke Niniwe dan berseru melawan kejahatannya. Niniwe adalah kota besar dalam kisah ini, tetapi Yunus justru pergi ke arah yang berlawanan. Masalah utama kitab mulai terlihat: Yunus tidak ingin melakukan tugas yang Tuhan berikan."),
("Badai di laut", "Yunus naik kapal dan para pelaut kemudian menghadapi badai besar. Mereka berusaha menyelamatkan kapal dan akhirnya mengetahui bahwa badai berkaitan dengan pelarian Yunus. Setelah Yunus berada di laut, Tuhan menyediakan ikan besar untuk menelannya."),
("Doa dari dalam kesesakan", "Di dalam ikan itu, Yunus berdoa dan mengakui bahwa keselamatan berasal dari Tuhan. Tuhan kemudian memerintahkan ikan itu dan Yunus kembali ke darat. Untuk kedua kalinya Tuhan memberikan perintah yang sama: pergi ke Niniwe."),
("Niniwe bertobat", "Kali ini Yunus pergi dan menyampaikan pesan Tuhan. Raja Niniwe—yang tidak disebut namanya—mendengar berita itu dan menyerukan pertobatan kepada seluruh kota. Penduduk Niniwe merespons, dan Tuhan melihat pertobatan mereka."),
("Yunus marah, Tuhan bertanya", "Yunus justru marah karena Tuhan mengampuni Niniwe. Tuhan memakai sebuah tanaman, ulat, dan angin untuk mengajar Yunus tentang belas kasih. Kitab berakhir dengan pertanyaan Tuhan tentang sebuah kota yang dikasihi-Nya. Pembaca dibiarkan memikirkan luasnya belas kasih Tuhan."),
],
"Mikha":[
("Mikha dari Moresyet", "Mikha berasal dari Moresyet dan bernubuat pada masa Yotam, Ahas, dan Hizkia. Ia melihat masyarakat Yehuda dan Israel yang mengalami ketidakadilan. Mikha berbicara sebagai nabi yang membela kebenaran Tuhan di tengah penyalahgunaan kekuasaan."),
("Pemimpin, imam, dan nabi", "Mikha menegur pemimpin yang mengambil keuntungan dari rakyat, imam yang melayani demi bayaran, dan nabi yang menyesuaikan pesan dengan kepentingan mereka. Masalahnya bukan sekadar satu orang, melainkan sistem kehidupan yang menjauh dari keadilan Tuhan."),
("Sion dan damai", "Setelah penghakiman, Mikha melihat masa ketika bangsa-bangsa datang belajar jalan Tuhan. Pedang akan ditempa menjadi alat pertanian dan manusia tidak lagi belajar berperang. Harapan ini menunjukkan bahwa tujuan Tuhan bukan kehancuran semata, melainkan damai yang lahir dari pemerintahan-Nya."),
("Betlehem dan seorang penguasa", "Mikha berbicara tentang Betlehem-Efrata, sebuah tempat kecil yang akan menjadi asal seorang penguasa bagi Israel. Dalam tradisi Kristen, bagian ini dibaca bersama kelahiran Yesus. Teks Mikha sendiri menempatkannya sebagai janji tentang seorang pemimpin yang menggembalakan umat."),
("Apa yang Tuhan kehendaki", "Dalam Mikha 6, Tuhan mengajukan perkara terhadap umat-Nya. Jawabannya diringkas dalam panggilan untuk berlaku adil, mencintai kesetiaan, dan hidup rendah hati di hadapan Tuhan. Jadi kehidupan bersama Tuhan terlihat dalam cara manusia memperlakukan sesamanya."),
("Menunggu dan berharap", "Mikha tidak menutup kitab dengan keberhasilan manusia, melainkan dengan penantian. Nabi menyatakan bahwa ia akan menunggu Tuhan. Pada akhirnya ia mengingat Tuhan yang mengampuni dan membuang dosa umat-Nya. Harapan berdiri di atas karakter Tuhan."),
],
"Nahum":[
("Nahum dan Niniwe", "Nahum dari Elkos membawa berita tentang Niniwe, ibu kota Asyur. Kota yang pernah muncul dalam kisah Yunus kini kembali menjadi pusat perhatian, tetapi suasananya berbeda. Nahum berbicara tentang penghakiman atas kekerasan dan penindasan Asyur."),
("Tuhan adalah tempat perlindungan", "Nahum tidak hanya berbicara tentang kehancuran musuh. Ia lebih dahulu menyatakan bahwa Tuhan itu baik dan menjadi tempat perlindungan pada waktu kesesakan. Bagi Yehuda yang pernah ditekan Asyur, keadilan Tuhan menjadi berita yang menguatkan."),
("Niniwe dikepung", "Gambaran pengepungan Niniwe menunjukkan kota yang selama ini tampak kuat akhirnya tidak mampu menyelamatkan dirinya. Nahum menggambarkan runtuhnya pertahanan dan berakhirnya kejayaan Asyur."),
("Kejahatan tidak kekal", "Pada penutup kitab, Nahum kembali menyebut kekerasan Niniwe. Penghakiman itu menjadi pesan bahwa kekuasaan yang dibangun di atas penindasan tidak akan berlangsung selamanya. Tuhan tetap menjadi hakim atas bangsa-bangsa."),
],
"Habakuk":[
("Habakuk bertanya", "Habakuk memulai kitab dengan pertanyaan yang jujur: mengapa kekerasan dan ketidakadilan seolah dibiarkan? Ia tidak menyembunyikan kebingungannya. Nabi membawa pertanyaan itu langsung kepada Tuhan."),
("Orang Kasdim datang", "Tuhan menjawab bahwa Ia sedang membangkitkan orang Kasdim untuk melakukan penghakiman. Jawaban itu justru membuat Habakuk semakin bingung karena bangsa yang akan dipakai itu sendiri terkenal keras. Nabi kembali bertanya tentang keadilan Tuhan."),
("Menunggu di menara", "Habakuk memutuskan berdiri di tempat pengintai dan menunggu jawaban Tuhan. Di sana ia menerima panggilan untuk menantikan penggenapan. Prinsip penting muncul: orang benar akan hidup oleh iman."),
("Celaka bagi yang sombong", "Tuhan menyatakan beberapa celaka terhadap keserakahan, kekerasan, dan penyembahan berhala. Babel tidak akan menjadi penguasa terakhir. Tuhan tetap memiliki batas bagi kesombongan manusia."),
("Dari keluhan menuju iman", "Dalam doa penutup, Habakuk mengingat karya Tuhan dan memilih bersukacita di dalam-Nya meskipun hasil tanah dan ternak tidak tersedia. Keadaannya belum tentu berubah, tetapi cara ia berdiri di hadapan Tuhan berubah: ia memilih percaya dan menantikan."),
],
"Zefanya":[
("Zefanya pada masa Yosia", "Zefanya bin Kusyi bernubuat pada masa Yosia, raja Yehuda. Ia memperingatkan bahwa Hari Tuhan akan datang. Pesannya menyentuh Yehuda dan bangsa-bangsa, karena tidak ada kelompok yang dapat menganggap dirinya kebal dari penghakiman Tuhan."),
("Hari Tuhan", "Zefanya menggambarkan Hari Tuhan sebagai hari kegentingan dan penghakiman. Dosa Yehuda, penyembahan berhala, dan ketidaksetiaan tidak dapat dibiarkan. Peringatan ini dimaksudkan untuk membawa umat menyadari keseriusan keadaan mereka."),
("Carilah Tuhan", "Di tengah berita penghakiman, Zefanya mengundang orang yang rendah hati untuk mencari Tuhan, keadilan, dan kerendahan hati. Harapan muncul bukan melalui kesombongan, tetapi melalui pertobatan."),
("Sisa umat", "Tuhan menjanjikan sisa umat yang dimurnikan. Mereka akan menjadi umat yang rendah hati dan tidak lagi hidup dalam penipuan. Pemulihan berarti Tuhan membentuk kembali komunitas yang dapat hidup dalam kebenaran."),
("Tuhan di tengah umat", "Penutup kitab berubah menjadi sangat lembut: Tuhan hadir di tengah umat-Nya, menyelamatkan, dan bersukacita atas mereka. Setelah berbicara tentang Hari Tuhan yang menggetarkan, Zefanya berakhir dengan kehadiran Tuhan sebagai sumber sukacita dan pemulihan."),
],
"Hagai":[
("Hagai melihat prioritas yang salah", "Pada tahun kedua pemerintahan Darius, nabi Hagai berbicara kepada Zerubabel, gubernur Yehuda, dan Yosua anak Yozadak, imam besar. Umat sudah kembali dari pembuangan tetapi rumah Tuhan masih terbengkalai. Mereka justru sibuk membangun rumah sendiri."),
("Perhatikan keadaanmu", "Hagai meminta umat memperhatikan hidup mereka. Mereka menabur banyak tetapi hasilnya sedikit; gambaran itu dipakai untuk menolong mereka melihat bahwa prioritas mereka telah berantakan. Firman Tuhan mengarahkan mereka kembali kepada pekerjaan yang telah mereka tinggalkan."),
("Zerubabel, Yosua, dan umat merespons", "Zerubabel, Yosua, dan seluruh umat mendengar firman Tuhan lalu mulai bekerja. Di sinilah cerita berubah. Ketaatan tidak lagi hanya menjadi wacana; umat benar-benar kembali membangun rumah Tuhan."),
("Jangan takut", "Ketika pembangunan berjalan, Tuhan berkata kepada Zerubabel, Yosua, dan umat: kuatkan hati dan bekerja, sebab Tuhan menyertai mereka. Ukuran keberhasilan bukan hanya kemegahan bangunan, tetapi kehadiran Tuhan di tengah umat yang taat."),
("Kemuliaan yang akan datang", "Hagai menutup dengan janji tentang kemuliaan rumah Tuhan dan perkataan khusus kepada Zerubabel. Tuhan menunjukkan bahwa Ia tetap bekerja melalui umat yang kembali. Masa depan mereka berada dalam tangan Tuhan, bukan sekadar dalam keadaan politik saat itu."),
],
"Zakharia":[
("Zakharia mengajak umat kembali", "Zakharia bin Berekhya bin Ido bernubuat pada masa pembangunan kembali Bait Allah. Pesan awalnya sederhana: kembalilah kepada Tuhan. Umat yang baru pulang dari pembuangan perlu memahami bahwa pemulihan fisik harus disertai pembaruan hubungan dengan Tuhan."),
("Para penunggang kuda", "Dalam penglihatan pertama, Zakharia melihat penunggang kuda dan menerima pesan bahwa Tuhan memperhatikan keadaan bumi. Penglihatan-penglihatan berikutnya menunjukkan bahwa kekuatan yang menekan umat tidak akan berkuasa selamanya."),
("Yosua dibersihkan", "Yosua anak Yozadak, imam besar, muncul dalam sebuah penglihatan di hadapan Tuhan. Ia berdiri dengan pakaian kotor dan kemudian diberi pakaian yang bersih. Penglihatan itu menggambarkan tindakan Tuhan membersihkan dan memulihkan kepemimpinan umat."),
("Zerubabel dan Roh Tuhan", "Zerubabel, gubernur Yehuda, memimpin pembangunan Bait Allah. Zakharia menerima penglihatan tentang kaki dian dan dua pohon zaitun, lalu menyampaikan prinsip bahwa pekerjaan itu berlangsung bukan terutama karena kekuatan manusia, melainkan oleh Roh Tuhan."),
("Raja yang rendah hati", "Zakharia kemudian melihat harapan tentang seorang Raja yang datang kepada Sion dengan rendah hati. Ia membawa keselamatan dan berbicara tentang damai bagi bangsa-bangsa. Dalam tradisi Kristen, bagian ini dikenali dalam kisah masuknya Yesus ke Yerusalem."),
("Gembala dan pemurnian", "Kitab juga berbicara tentang gembala, pemurnian, dan penderitaan umat. Gambaran-gambaran ini menunjukkan bahwa pemulihan tidak selalu berarti jalan tanpa kesulitan. Tuhan memurnikan umat agar mereka kembali menjadi milik-Nya."),
("Tuhan menjadi Raja", "Penglihatan terakhir membawa pembaca kepada Hari Tuhan. Kekuasaan manusia tidak menjadi pusat akhir cerita. Tuhan sendiri digambarkan sebagai Raja atas seluruh bumi, dan Yerusalem menjadi bagian dari gambaran pemerintahan-Nya."),
],
"Maleakhi":[
("Maleakhi dan pertanyaan tentang kasih", "Kitab Maleakhi dibuka dengan perkataan Tuhan bahwa Ia mengasihi umat-Nya. Umat menjawab dengan pertanyaan, 'Dengan cara bagaimanakah Engkau mengasihi kami?' Dari sini terlihat masalah utama: hati umat sudah dingin dan mereka mempertanyakan kasih Tuhan."),
("Para imam tidak menghormati Tuhan", "Para imam menjadi pusat teguran. Mereka mempersembahkan korban yang tidak layak dan tidak menghormati nama Tuhan. Masalah ibadah ternyata bukan kurangnya aktivitas, melainkan hilangnya rasa hormat kepada Tuhan yang mereka layani."),
("Perjanjian dan kehidupan umat", "Maleakhi menegur para imam karena gagal menjaga perjanjian dan menegur umat karena ketidaksetiaan dalam kehidupan mereka. Tuhan tidak memisahkan ibadah dari karakter. Kesetiaan kepada-Nya harus terlihat dalam hubungan, kejujuran, dan cara umat menjalani perjanjian."),
("Utusan yang mempersiapkan jalan", "Tuhan menjanjikan seorang utusan yang mempersiapkan jalan. Sesudah itu Tuhan datang untuk memurnikan umat seperti api pemurni logam. Pesannya bukan hanya penghukuman, tetapi proses membersihkan umat agar ibadah mereka kembali benar."),
("Kembalilah kepada-Ku", "Tuhan memanggil umat untuk kembali kepada-Nya. Mereka dipanggil untuk berhenti dari ketidaksetiaan dan kembali menghormati Tuhan. Maleakhi menunjukkan bahwa pemulihan hubungan dimulai ketika umat menjawab panggilan itu dengan sungguh-sungguh."),
("Hari Tuhan dan Elia", "Kitab berakhir dengan Hari Tuhan yang besar dan dahsyat. Tuhan menyebut Elia sebagai nabi yang akan diutus sebelum hari itu, dengan tujuan membawa hati berbalik. Identitas 'Maleakhi' sendiri tidak dijelaskan lebih jauh dalam kitab; yang terutama adalah pesan Tuhan yang dibawanya. Perjalanan 17 kitab berakhir dengan sebuah panggilan: kembali kepada Tuhan dan bersiap menyambut karya-Nya."),
],
}

VERSE_DATA = {
    "Yesaya": [("Yes 6:3", "Tuhan dinyatakan kudus; kekudusan menjadi titik awal panggilan Yesaya."), ("Yes 6:8", "Yesaya siap diutus oleh Tuhan."), ("Yes 7:14", "Tanda Imanuel sebagai janji di tengah krisis."), ("Yes 9:5-6", "Harapan tentang Raja yang membawa damai."), ("Yes 40:31", "Orang yang menanti Tuhan menerima kekuatan baru."), ("Yes 53:4-6", "Hamba Tuhan menanggung penderitaan bagi manusia."), ("Yes 65:17", "Gambaran langit baru dan bumi baru.")],
    "Yeremia": [("Yer 1:5", "Panggilan Yeremia diletakkan dalam rencana Tuhan sejak sebelum kelahirannya."), ("Yer 2:13", "Israel meninggalkan sumber air hidup."), ("Yer 7:23", "Tuhan menuntut ketaatan dan mendengar suara-Nya."), ("Yer 17:7-8", "Orang yang mengandalkan Tuhan adalah seperti pohon dekat air."), ("Yer 29:11", "Janji masa depan dan damai untuk umat dalam pembuangan."), ("Yer 31:31-34", "Perjanjian baru yang ditulis dalam hati.")],
    "Ratapan": [("Rat 3:21-23", "Di tengah penderitaan, kasih setia Tuhan tetap ada."), ("Rat 3:25-26", "Tuhan tetap menanti orang yang mencari-Nya."), ("Rat 5:21", "Doa pemulihan umat." )],
    "Yehezkiel": [("Yeh 1:28", "Penglihatan kemuliaan Tuhan."), ("Yeh 3:17", "Yehezkiel ditetapkan sebagai penjaga."), ("Yeh 18:23", "Tuhan menghendaki pertobatan."), ("Yeh 36:26-27", "Hati baru dan roh baru."), ("Yeh 37:1-14", "Lembah tulang kering memberi gambaran pemulihan."), ("Yeh 48:35", "Nama kota menegaskan kehadiran Tuhan.")],
    "Daniel": [("Dan 1:8", "Daniel menetapkan hati untuk setia kepada Tuhan."), ("Dan 2:20-22", "Hikmat dan rahasia berasal dari Tuhan."), ("Dan 3:17-18", "Kesetiaan yang tak tergoyahkan."), ("Dan 4:37", "Nebukadnezar mengakui kuasa Tuhan."), ("Dan 6:10", "Daniel tetap berdoa."), ("Dan 7:13-14", "Anak Manusia menerima pemerintahan yang kekal."), ("Dan 12:2", "Kebangkitan dan masa depan." )],
    "Hosea": [("Hos 2:19-20", "Hubungan yang dipulihkan dalam kasih setia."), ("Hos 6:6", "Tuhan menginginkan kasih setia lebih dari ritual."), ("Hos 11:1", "Israel adalah anak yang dikasihi Tuhan."), ("Hos 11:8-9", "Belas kasih Tuhan sangat besar."), ("Hos 14:2-5", "Panggilan kembali dan penyembuhan." )],
    "Yoel": [("Yl 2:12-13", "Umat dipanggil bertobat dengan hati."), ("Yl 2:25", "Tuhan menjanjikan pemulihan atas tahun-tahun yang hilang."), ("Yl 2:28-29", "Pencurahan Roh."), ("Yl 3", "Bangsa-bangsa diadili dan Tuhan menjadi perlindungan." )],
    "Amos": [("Am 3:3", "Hubungan dan kesepakatan di antara dua pihak."), ("Am 5:14-15", "Mencari yang baik dan menegakkan keadilan."), ("Am 5:24", "Keadilan harus mengalir seperti sungai."), ("Am 7:14-15", "Tuhan mengambil dan mengutus Amos."), ("Am 9:11", "Janji pemulihan." )],
    "Obaja": [("Ob 3-4", "Kesombongan Edom tidak dapat menyelamatkan mereka."), ("Ob 12", "Edom ditegur karena sikapnya terhadap Yerusalem."), ("Ob 15", "Hari Tuhan membawa prinsip menuai sesuai perbuatan."), ("Ob 21", "Akhir kitab berbicara tentang kerajaan Tuhan.")],
    "Yunus": [("Yun 1:3", "Yunus melarikan diri dari tugas Tuhan."), ("Yun 1:17", "Tuhan menyediakan ikan besar."), ("Yun 2:9", "Keselamatan berasal dari Tuhan."), ("Yun 3:5-10", "Niniwe bertobat."), ("Yun 4:11", "Pertanyaan terakhir tentang belas kasih Tuhan.")],
    "Mikha": [("Mi 4:1-5", "Sion dan damai dalam jalan Tuhan."), ("Mi 5:1", "Betlehem tempat penguasa lahir."), ("Mi 6:8", "Berlaku adil, kasih setia, dan rendah hati."), ("Mi 7:7", "Menunggu Tuhan."), ("Mi 7:18-19", "Tuhan mengampuni dan membuang dosa." )],
    "Nahum": [("Nah 1:7", "Tuhan adalah tempat perlindungan."), ("Nah 2", "Niniwe dikepung dan runtuh."), ("Nah 3:5-7", "Kejahatan Niniwe mendapat penghakiman.")],
    "Habakuk": [("Hab 1:2-4", "Habakuk mengeluh tentang ketidakadilan."), ("Hab 1:12-13", "Tuhan memakai bangsa yang jahat untuk penghakiman."), ("Hab 2:4", "Orang benar hidup oleh iman."), ("Hab 3:17-18", "Sukacita di tengah keadaan sulit." )],
    "Zefanya": [("Zef 1:14-18", "Hari Tuhan sebagai hari penghakiman."), ("Zef 2:3", "Mencari Tuhan, keadilan, dan kerendahan hati."), ("Zef 3:9", "Pemurnian umat agar memanggil nama Tuhan."), ("Zef 3:17", "Tuhan hadir di tengah umat dan bersukacita atas mereka.")],
    "Hagai": [("Hag 1:5-7", "Perhatikan keadaan hidup dan prioritas."), ("Hag 1:12", "Umat mulai lagi bekerja."), ("Hag 2:4", "Tuhan menyertai pekerjaan mereka."), ("Hag 2:9", "Kemuliaan rumah Tuhan yang akan datang.")],
    "Zakharia": [("Za 1:3", "Kembali kepada Tuhan."), ("Za 3:4", "Pembersihan dan pemulihan Yosua."), ("Za 4:6", "Pekerjaan Tuhan melalui Roh, bukan kekuatan manusia."), ("Za 9:9", "Raja yang datang dengan rendah hati."), ("Za 14:9", "Tuhan menjadi Raja atas seluruh bumi.")],
    "Maleakhi": [("Mal 1:2", "Umat mempertanyakan kasih Tuhan."), ("Mal 1:6", "Para imam tidak menghormati nama Tuhan."), ("Mal 3:1", "Utusan yang mempersiapkan jalan."), ("Mal 3:7", "Panggilan untuk kembali kepada Tuhan."), ("Mal 3:16-18", "Orang yang takut akan Tuhan diperhatikan."), ("Mal 4:5-6", "Janji tentang Elia sebelum Hari Tuhan.")],
}

CHAPTERS = {
    "Yesaya": 66,
    "Yeremia": 52,
    "Ratapan": 5,
    "Yehezkiel": 48,
    "Daniel": 12,
    "Hosea": 14,
    "Yoel": 3,
    "Amos": 9,
    "Obaja": 1,
    "Yunus": 4,
    "Mikha": 7,
    "Nahum": 3,
    "Habakuk": 3,
    "Zefanya": 3,
    "Hagai": 2,
    "Zakharia": 14,
    "Maleakhi": 4,
}

QUESTION_BANK = [
    ("Yesaya", "Urutkan perjalanan Yesaya: panggilan, krisis Ahas, Hizkia menghadapi Asyur, peringatan Babel, Hamba Tuhan, ciptaan baru.", "Panggilan (Yes 6), Ahas/Imanuel (7), Hizkia/Asyur (36–39), Babel dan penghiburan (40 dst.), Hamba (52–53), ciptaan baru (65–66)."),
    ("Yeremia", "Mengapa khotbah di pintu Bait Allah menjadi penting?", "Karena umat menganggap Bait Allah menjamin keamanan, sementara Tuhan menuntut pertobatan, keadilan, dan ketaatan."),
    ("Ratapan", "Mengapa Ratapan 3 menjadi titik balik?", "Keadaan belum pulih, tetapi penulis mengingat kasih setia Tuhan dan menemukan alasan untuk berharap."),
    ("Yehezkiel", "Apa hubungan penjaga, hati baru, dan tulang kering?", "Yehezkiel memperingatkan umat, lalu Tuhan menjanjikan pembaruan dari dalam dan pemulihan umat yang tampak tanpa harapan."),
    ("Daniel", "Apa benang merah Dan 2, 3, 6, dan 7?", "Manusia dan kerajaan dapat berubah, tetapi Tuhan berdaulat; umat dipanggil tetap setia."),
    ("Hosea", "Mengapa kisah pernikahan Hosea menjadi gambaran teologis?", "Ketidaksetiaan Gomer menjadi simbol ketidaksetiaan Israel, sedangkan kasih Tuhan tetap memanggil umat kembali."),
    ("Yoel", "Bagaimana kitab bergerak dari belalang menuju Roh Tuhan?", "Krisis → pertobatan → pemulihan → pencurahan Roh → penghakiman bangsa-bangsa."),
    ("Amos", "Mengapa Am 5:24 penting untuk memahami kitab?", "Karena keadilan bukan tambahan kecil bagi ibadah; keadilan merupakan bagian dari kehidupan yang Tuhan kehendaki."),
    ("Obaja", "Apa yang membuat dosa Edom lebih serius ketika Yerusalem jatuh?", "Mereka tidak menolong saudaranya dan malah bersukacita serta mengambil keuntungan dari bencana."),
    ("Yunus", "Bandingkan Niniwe dalam Yunus dan Nahum.", "Yunus menampilkan pertobatan Niniwe; Nahum menampilkan penghakiman atas Niniwe/Asyur."),
    ("Mikha", "Sebutkan tiga unsur Mi 6:8 dan hubungkan dengan kritik sosial Mikha.", "Berlaku adil, mengasihi kesetiaan, dan hidup rendah hati bersama Tuhan."),
    ("Nahum", "Mengapa pesan Nahum juga dapat disebut penghiburan bagi Yehuda?", "Karena kejatuhan kekuatan Asyur berarti berakhirnya salah satu sumber penindasan."),
    ("Habakuk", "Apa perubahan Habakuk dari pasal 1 ke pasal 3?", "Dari keluhan dan kebingungan menuju penantian, iman, doa, dan sukacita dalam Tuhan."),
    ("Zefanya", "Bagaimana Hari Tuhan dan pemulihan terhubung?", "Penghakiman membersihkan dan diikuti janji tentang sisa umat serta kehadiran Tuhan."),
    ("Hagai", "Apa titik balik utama kitab?", "Zerubabel, Yosua, dan umat merespons firman lalu mulai membangun kembali Bait Allah."),
    ("Zakharia", "Apa pesan Za 4:6 dalam konteks pembangunan kembali?", "Pekerjaan Tuhan tidak terutama bergantung pada kekuatan manusia, melainkan pada Roh Tuhan."),
    ("Maleakhi", "Apa masalah rohani yang berulang dalam Maleakhi?", "Kurangnya hormat dan kesetiaan dalam ibadah, kepemimpinan imam, perjanjian, dan kehidupan umat."),
]



# --- VISUAL / NAVIGATION ---
BG = (10, 13, 22)
SURFACE = (19, 23, 34)
SURFACE_2 = (27, 32, 45)
IVORY = (244, 239, 227)
MUTED = (164, 167, 175)
GOLD = (211, 177, 96)
GOLD_SOFT = (133, 111, 67)
LINE = (55, 59, 70)

FONT = pygame.font.SysFont("georgia", 20)
SMALL = pygame.font.SysFont("segoeui", 15)
BODY = pygame.font.SysFont("georgia", 21)
BIG = pygame.font.SysFont("georgia", 30, bold=True)
TITLE = pygame.font.SysFont("georgia", 56, bold=True)

BOOK_IDS = {name: i + 1 for i, (name, *_rest) in enumerate(BOOKS)}

CHARACTER_GUIDE = {
    "Yesaya": {
        "Yesaya": "Nabi dari Yehuda, anak Amos. Ia dipanggil Tuhan dan menyampaikan firman kepada Yehuda pada masa Uzia, Yotam, Ahas, dan Hizkia.",
        "Ahas": "Raja Yehuda dan anak Yotam. Ketika Aram dan Israel mengancam Yerusalem, ia memilih mencari pertolongan Asyur daripada mempercayai Tuhan.",
        "Hizkia": "Raja Yehuda dan anak Ahas. Dalam krisis Asyur, ia membawa ancaman itu kepada Tuhan dan menjadi bagian penting dari kisah pemeliharaan Yerusalem.",
        "Sennakerib": "Raja Asyur yang menyerang kota-kota Yehuda dan mengepung Yerusalem. Dalam kisah Yesaya, kekuasaannya tetap berada di bawah kedaulatan Tuhan.",
        "Rezin": "Raja Aram yang bersama Pekah menekan Yehuda pada masa Ahas.",
        "Pekah": "Raja Israel yang bersekutu dengan Rezin melawan Yehuda.",
    },
    "Yeremia": {
        "Yeremia": "Nabi dari Anatot, anak Hilkia. Tuhan memanggilnya sejak muda untuk menyampaikan firman kepada Yehuda menjelang dan selama kehancuran Yerusalem.",
        "Barukh": "Juru tulis dan pendamping Yeremia. Ia menuliskan perkataan yang disampaikan Yeremia dan membantu menyampaikannya kepada umat.",
        "Yosia": "Raja Yehuda yang melakukan pembaruan keagamaan. Pada masanya Yeremia mulai menjalankan panggilannya sebagai nabi.",
        "Yoyakim": "Raja Yehuda yang pemerintahannya berhadapan dengan pesan-pesan keras Yeremia tentang penghakiman yang mendekat.",
        "Zedekia": "Raja terakhir Yehuda sebelum jatuhnya Yerusalem. Ia berulang kali berhadapan dengan perkataan Yeremia.",
        "Nebukadnezar": "Raja Babel yang menjadi tokoh politik utama dalam masa kejatuhan Yerusalem dan pembuangan Yehuda.",
        "Hananya": "Nabi yang menyampaikan nubuat damai yang bertentangan dengan pesan Yeremia tentang kuk Babel.",
    },
    "Ratapan": {
        "Penyair": "Suara manusia yang meratap atas kehancuran Yerusalem. Ia tidak menyembunyikan luka, tetapi juga mengingat kasih setia Tuhan.",
        "Yerusalem": "Kota yang telah dihancurkan dan dalam puisi digambarkan seperti seorang perempuan yang berduka.",
        "Umat Yehuda": "Mereka mengalami perang, kelaparan, pembuangan, dan kehilangan tempat hidup mereka.",
    },
    "Yehezkiel": {
        "Yehezkiel": "Imam yang dipanggil Tuhan menjadi nabi di tengah orang-orang Yehuda yang dibuang ke Babel.",
        "Para tua-tua": "Pemimpin umat yang datang kepada Yehezkiel untuk mencari jawaban dari Tuhan.",
        "Umat buangan": "Orang-orang Yehuda yang hidup di Babel dan harus memahami bahwa Tuhan tetap berdaulat meski Yerusalem telah jatuh.",
        "Gog": "Tokoh dalam nubuat penghakiman terhadap kekuatan yang datang melawan umat Tuhan.",
    },
    "Daniel": {
        "Daniel": "Orang Yehuda yang hidup di lingkungan kerajaan Babel dan kemudian Persia. Ia dikenal karena kesetiaannya kepada Tuhan di tengah kekuasaan asing.",
        "Sadrakh": "Salah satu sahabat Daniel yang bersama Mesakh dan Abednego menolak menyembah patung yang diperintahkan Nebukadnezar.",
        "Mesakh": "Sahabat Daniel yang tetap setia kepada Tuhan ketika diperhadapkan pada perintah raja.",
        "Abednego": "Sahabat Daniel yang bersama dua rekannya menghadapi hukuman karena tidak menyembah patung.",
        "Nebukadnezar": "Raja Babel yang menerima Daniel dan sahabat-sahabatnya dalam lingkungan kerajaan, sekaligus menjadi tokoh dalam beberapa mimpi dan ujian mereka.",
        "Belsyazar": "Raja yang tampil dalam kisah pesta besar dan tulisan di dinding yang ditafsirkan Daniel.",
        "Darius": "Raja dalam kisah Daniel 6. Identitas historis tokoh ini diperdebatkan, sehingga tidak sebaiknya disamakan secara pasti dengan satu tokoh lain.",
        "Gabriel": "Utusan surgawi yang datang menjelaskan penglihatan Daniel dalam bagian-bagian kitab tertentu.",
    },
    "Hosea": {
        "Hosea": "Nabi dari Israel utara. Melalui kehidupan keluarganya, Tuhan memakai pengalaman pribadi Hosea sebagai gambaran hubungan perjanjian dengan Israel.",
        "Gomer": "Istri Hosea yang menjadi bagian dari tanda profetis tentang ketidaksetiaan Israel kepada Tuhan.",
        "Anak-anak Hosea": "Nama-nama mereka menjadi tanda pesan Tuhan tentang keadaan dan masa depan Israel.",
        "Umat Israel": "Bangsa yang terus-menerus berpaling kepada berhala, tetapi tetap dipanggil Tuhan untuk kembali.",
    },
    "Yoel": {
        "Yoel": "Nabi yang menyampaikan pesan tentang bencana belalang, Hari Tuhan, pertobatan, pemulihan, dan pencurahan Roh.",
        "Imam": "Pelayan ibadah yang dipanggil untuk mengumpulkan umat dalam pertobatan dan doa.",
        "Umat Yehuda": "Mereka menghadapi krisis dan dipanggil untuk kembali kepada Tuhan dengan segenap hati.",
    },
    "Amos": {
        "Amos": "Peternak dan pemungut buah dari Tekoa yang dipanggil Tuhan untuk bernubuat kepada Israel utara, terutama menegur ketidakadilan sosial.",
        "Amazia": "Imam di Betel yang menolak pesan Amos dan meminta Amos pergi dari wilayah Israel.",
        "Yerobeam II": "Raja Israel pada masa Amos bernubuat. Masa pemerintahannya menjadi latar bagi kritik terhadap ketimpangan dan ketidakadilan.",
        "Orang miskin": "Kelompok yang ditindas oleh sistem ekonomi dan hukum yang tidak adil, menjadi perhatian besar dalam teguran Amos.",
    },
    "Obaja": {
        "Obaja": "Nama nabi yang menyampaikan pesan penghakiman terhadap Edom dan pemulihan bagi Sion.",
        "Edom": "Bangsa yang terkait dengan Israel melalui garis keturunan Esau-Yakub. Obaja menegur sikap Edom ketika Yerusalem jatuh.",
        "Yehuda": "Umat yang mengalami kehancuran Yerusalem tetapi menerima janji bahwa Tuhan akan memulihkan Sion.",
    },
    "Yunus": {
        "Yunus": "Nabi anak Amitai yang diutus Tuhan ke Niniwe. Ia justru melarikan diri dan kemudian harus belajar tentang belas kasihan Tuhan.",
        "Pelaut": "Orang-orang di kapal yang mengalami badai ketika Yunus melarikan diri. Mereka akhirnya takut kepada Tuhan.",
        "Raja Niniwe": "Penguasa yang tidak disebut namanya. Setelah mendengar pesan Yunus, ia menyerukan pertobatan kepada seluruh kota.",
        "Penduduk Niniwe": "Orang-orang yang bertobat ketika mendengar pemberitaan Yunus.",
    },
    "Mikha": {
        "Mikha": "Nabi dari Moresyet yang menegur pemimpin dan orang kaya karena penindasan, sekaligus menyampaikan harapan tentang pemulihan.",
        "Pemimpin": "Kelompok penguasa yang ditegur karena memakai kekuasaan untuk keuntungan sendiri.",
        "Imam": "Pemimpin keagamaan yang disebut dalam kritik Mikha terhadap penyalahgunaan pelayanan demi keuntungan.",
        "Umat": "Masyarakat yang dipanggil kembali kepada keadilan, kesetiaan, dan kerendahan hati di hadapan Tuhan.",
    },
    "Nahum": {
        "Nahum": "Nabi dari Elkos yang menyampaikan nubuat tentang jatuhnya Niniwe dan berakhirnya kekuasaan Asyur.",
        "Niniwe": "Ibu kota Asyur yang menjadi sasaran penghakiman karena kekerasan dan penindasan.",
        "Yehuda": "Umat yang menerima kabar bahwa kekuatan Asyur yang menindas tidak akan bertahan selamanya.",
    },
    "Habakuk": {
        "Habakuk": "Nabi yang membawa pertanyaan jujur tentang kejahatan dan keadilan kepada Tuhan, lalu belajar menantikan jawaban-Nya.",
        "Orang Kasdim": "Bangsa yang Tuhan sebut dalam jawaban kepada Habakuk sebagai alat penghakiman, sekaligus bangsa yang juga akan dihakimi.",
    },
    "Zefanya": {
        "Zefanya": "Nabi yang berbicara tentang Hari Tuhan, penghakiman, pemurnian, dan pemulihan umat yang rendah hati.",
        "Yosia": "Raja Yehuda yang menjadi latar pemerintahan Zefanya. Pada masa itu berlangsung pembaruan keagamaan.",
        "Sisa umat": "Kelompok yang rendah hati dan mencari Tuhan, yang menerima janji pemulihan.",
    },
    "Hagai": {
        "Hagai": "Nabi pada masa sesudah pembuangan yang mendorong umat memprioritaskan pembangunan kembali Bait Allah.",
        "Zerubabel": "Bupati atau gubernur Yehuda pada masa itu dan keturunan Daud yang menjadi pemimpin pembangunan kembali.",
        "Yosua": "Imam besar yang memimpin pelayanan umat bersama Zerubabel.",
        "Umat": "Orang-orang yang kembali dari pembuangan dan dipanggil untuk membangun kembali rumah Tuhan.",
    },
    "Zakharia": {
        "Zakharia": "Nabi pada masa pembangunan kembali Bait Allah. Penglihatannya menguatkan umat bahwa pekerjaan itu berada dalam penyertaan Tuhan.",
        "Zerubabel": "Gubernur Yehuda yang menjadi pemimpin pembangunan Bait Allah.",
        "Yosua": "Imam besar yang dipulihkan dalam penglihatan Zakharia dan menjadi lambang pemulihan kepemimpinan umat.",
        "Malaikat Tuhan": "Tokoh surgawi yang muncul dalam beberapa penglihatan Zakharia untuk menyampaikan pesan dan menjelaskan maknanya.",
    },
    "Maleakhi": {
        "Maleakhi": "Nama yang muncul dalam kitab sebagai pembawa pesan Tuhan; makna namanya berkaitan dengan 'utusan-Ku', dan identitas pribadinya tidak dijelaskan lebih jauh.",
        "Para imam": "Pemimpin ibadah yang ditegur karena tidak menghormati nama Tuhan dalam pelayanan dan korban.",
        "Umat": "Bangsa yang berulang kali mempertanyakan Tuhan dan dipanggil untuk kembali setia kepada perjanjian.",
        "Utusan": "Tokoh yang disebut akan mempersiapkan jalan sebelum Tuhan datang untuk menghakimi dan memurnikan.",
        "Elia": "Nabi yang disebut dalam penutup kitab sebagai tokoh yang akan diutus sebelum datangnya Hari Tuhan.",
    },
}

def wrap_text(text, font, max_width):
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        current = ""
        for word in words:
            test = word if not current else current + " " + word
            if font.size(test)[0] <= max_width:
                current = test
            else:
                if current: lines.append(current)
                current = word
        if current: lines.append(current)
        elif not words: lines.append("")
    return lines

def text_blit(text, x, y, font=FONT, color=IVORY, max_width=None):
    """Draw text safely; optionally clip/ellipsize to a maximum width."""
    if max_width is not None:
        text = str(text)
        if font.size(text)[0] > max_width:
            ell = "…"
            while text and font.size(text + ell)[0] > max_width:
                text = text[:-1]
            text = text.rstrip() + ell
    surf = font.render(str(text), True, color)
    screen.blit(surf, (int(x), int(y)))

def card(rect, fill=SURFACE, border=LINE, radius=18):
    rect = pygame.Rect(rect)
    pygame.draw.rect(screen, fill, rect, border_radius=radius)
    pygame.draw.rect(screen, border, rect, 1, border_radius=radius)

def draw_background():
    screen.fill(BG)
    # very subtle grid and horizon, kept intentionally quiet
    for x in range(0, WINDOW_WIDTH, 160):
        pygame.draw.line(screen, (14, 18, 28), (x, 0), (x, WINDOW_HEIGHT), 1)
    pygame.draw.line(screen, (31, 35, 46), (70, 122), (1210, 122), 1)
    for x, y, r in [(90,78,1),(210,132,1),(1035,82,1),(1170,176,1),(1210,620,1),(880,692,1),(320,650,1)]:
        pygame.draw.circle(screen, (86, 86, 91), (x,y), r)

def header(kicker, title, index=None):
    text_blit(kicker.upper(), 70, 43, SMALL, GOLD, 820)
    text_blit(title, 70, 67, BIG, IVORY, 820)
    if index is not None:
        text_blit(f"{index:02d} / 17", 1110, 54, SMALL, MUTED, 90)
    pygame.draw.line(screen, LINE, (70, 122), (1210, 122), 1)

def button(rect, label, active=False):
    rect = pygame.Rect(rect)
    fill = SURFACE_2 if active else SURFACE
    border = GOLD_SOFT if active else LINE
    pygame.draw.rect(screen, fill, rect, border_radius=10)
    pygame.draw.rect(screen, border, rect, 1, border_radius=10)
    f = SMALL
    for size in (15, 14, 13, 12):
        candidate = pygame.font.SysFont("segoeui", size)
        if candidate.size(label)[0] <= rect.w - 22:
            f = candidate; break
    w, h = f.size(label)
    screen.blit(f.render(label, True, IVORY if active else MUTED), (rect.centerx-w//2, rect.centery-h//2))

def open_bible(book, chapter=1, verse=None):
    q = f"{book} {chapter}" + (f":{verse}" if verse else "")
    webbrowser.open("https://alkitab.sabda.org/home.php?search=" + quote_plus(q))

def open_study(book):
    bid = BOOK_IDS[book]
    webbrowser.open(f"https://alkitab.sabda.org/commentary.php?book={bid}")

def open_encyclopedia(term):
    webbrowser.open("https://alkitab.sabda.org/dictionary.php?word=" + quote_plus(term))

def scene_people(book, narrative):
    people = CHARACTER_GUIDE.get(book, {})
    found = []
    low = narrative.lower()
    for name in people:
        if name.lower() in low:
            found.append(name)
    return found[:3]

def draw_story_text(narrative, x, y, width, height):
    lines = wrap_text(narrative, BODY, width)
    line_h = 30
    max_lines = max(1, (height - 4) // line_h)
    visible = lines[:max_lines]
    for i, line in enumerate(visible):
        text_blit(line, x, y + i*line_h, BODY, IVORY, width)
    if len(lines) > max_lines and visible:
        last = visible[-1]
        # Keep the final line visually inside the card.
        ell = "…"
        while last and BODY.size(last + ell)[0] > width:
            last = last[:-1]
        screen.fill(SURFACE, (x, y + (max_lines-1)*line_h, width, line_h))
        text_blit(last.rstrip()+ell, x, y + (max_lines-1)*line_h, BODY, IVORY, width)

def story_screen(book, scene_index):
    scenes = STORIES[book]
    while True:
        draw_background()
        idx = [b[0] for b in BOOKS].index(book) + 1
        title, narrative = scenes[scene_index]
        header(book, title, idx)

        story_rect = pygame.Rect(70, 145, 720, 430)
        card(story_rect, SURFACE)
        text_blit(f"BAGIAN {scene_index+1:02d}", 102, 175, SMALL, GOLD)
        draw_story_text(narrative, 102, 215, 656, 330)

        char_rect = pygame.Rect(815, 145, 395, 250)
        card(char_rect, SURFACE)
        text_blit("TOKOH", 845, 174, SMALL, GOLD)
        people = scene_people(book, narrative)
        guide = CHARACTER_GUIDE.get(book, {})
        yy = 208
        for person in people:
            text_blit(person, 845, yy, FONT, IVORY, 325)
            yy += 29
            desc_lines = wrap_text(guide.get(person, ""), SMALL, 325)
            for line in desc_lines[:2]:
                text_blit(line, 845, yy, SMALL, MUTED, 325); yy += 19
            yy += 10
            if yy > 370: break
        if not people:
            text_blit("—", 845, 210, FONT, MUTED)

        verse_rect = pygame.Rect(815, 415, 395, 160)
        card(verse_rect, SURFACE)
        text_blit("AYAT PENTING", 845, 444, SMALL, GOLD)
        verses = VERSE_DATA.get(book, [])
        if verses:
            vref, vmeaning = verses[min(scene_index, len(verses)-1)]
            text_blit(vref, 845, 473, FONT, IVORY, 325)
            for j, line in enumerate(wrap_text(vmeaning, SMALL, 325)[:3]):
                text_blit(line, 845, 504+j*19, SMALL, MUTED, 325)

        button((70, 665, 135, 44), "SEBELUMNYA", scene_index > 0)
        button((220, 665, 125, 44), "ALKITAB")
        button((360, 665, 105, 44), "STUDI")
        button((480, 665, 160, 44), "ENSIKLOPEDIA")
        button((1070, 665, 140, 44), "LANJUT", True)
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT: quit_game()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE: return
                if e.key == pygame.K_LEFT and scene_index > 0: scene_index -= 1
                elif e.key == pygame.K_RIGHT:
                    if scene_index < len(scenes)-1: scene_index += 1
                    else: return after_story_screen(book)
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                p = e.pos
                if pygame.Rect(70,665,135,44).collidepoint(p) and scene_index > 0: scene_index -= 1
                elif pygame.Rect(220,665,125,44).collidepoint(p): open_bible(book, scene_index + 1)
                elif pygame.Rect(360,665,105,44).collidepoint(p): open_study(book)
                elif pygame.Rect(480,665,160,44).collidepoint(p):
                    people = scene_people(book, narrative)
                    open_encyclopedia(people[0] if people else book)
                elif pygame.Rect(1070,665,140,44).collidepoint(p):
                    if scene_index < len(scenes)-1: scene_index += 1
                    else: return after_story_screen(book)

def after_story_screen(book):
    while True:
        draw_background(); idx=[b[0] for b in BOOKS].index(book)+1
        header("SELESAI", book, idx)
        text_blit("Perjalanan kitab ini selesai.",70,160,BODY,IVORY)
        card((70,215,1140,305),SURFACE)
        text_blit("JEJAK KITAB",105,248,SMALL,GOLD)
        meta=next(b for b in BOOKS if b[0]==book)
        text_blit(meta[1],105,285,SMALL,IVORY,1000)
        text_blit(meta[2],105,318,SMALL,MUTED,1000)
        text_blit(meta[3],105,351,SMALL,MUTED,1000)
        text_blit(meta[4],105,384,SMALL,MUTED,1000)
        button((70,665,125,44),"TOKOH",True); button((210,665,125,44),"ALKITAB"); button((350,665,105,44),"STUDI"); button((470,665,160,44),"ENSIKLOPEDIA"); button((1070,665,140,44),"PILIH KITAB",True)
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT: quit_game()
            if e.type==pygame.KEYDOWN and e.key==pygame.K_ESCAPE:return
            if e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
                p=e.pos
                if pygame.Rect(70,665,125,44).collidepoint(p): character_screen(book)
                elif pygame.Rect(210,665,125,44).collidepoint(p): open_bible(book)
                elif pygame.Rect(350,665,105,44).collidepoint(p): open_study(book)
                elif pygame.Rect(470,665,160,44).collidepoint(p): open_encyclopedia(book)
                elif pygame.Rect(1070,665,140,44).collidepoint(p): return select_book()

PROPHECY_DETAIL = {
    "Yesaya": [
        ("Imanuel", "Yesaya 7:10-14", "Dalam krisis Aram dan Israel/Efraim melawan Yehuda, Tuhan memberi tanda kepada Ahas.", "Yerusalem/Yehuda", "Matius 1:22-23 mengutip Yesaya 7:14 dalam kisah kelahiran Yesus. Konteks awalnya adalah krisis Ahas, sedangkan Matius membacanya dalam terang Kristus."),
        ("Raja dari garis Daud", "Yesaya 9:1-6; 11:1-10", "Seorang anak dari garis Daud digambarkan memerintah dengan keadilan, damai, dan Roh Tuhan.", "Yehuda; kerajaan Daud", "Lukas 1:32-33 dan tema pemerintahan Yesus sering dibaca bersama janji Daud. Penggenapan penuh kerajaan damai tetap menjadi pengharapan eskatologis."),
        ("Hamba yang menderita", "Yesaya 52:13-53:12", "Hamba Tuhan ditolak, menderita, menanggung dosa banyak orang, lalu ditinggikan.", "Dalam nubuat Yesaya; tidak diberi lokasi kejadian historis tertentu", "Kisah Para Rasul 8:32-35 menerapkan bagian ini kepada Yesus; 1 Petrus 2:24 juga memakai gambaran penderitaan Hamba."),
        ("Keselamatan bagi bangsa-bangsa", "Yesaya 42:1-9; 49:5-7", "Hamba menjadi terang bagi bangsa-bangsa sehingga keselamatan Tuhan menjangkau jauh melampaui Israel.", "Israel dan bangsa-bangsa", "Lukas 2:32 menyebut Yesus terang bagi bangsa-bangsa; Kisah Para Rasul juga memperluas misi keselamatan kepada bangsa-bangsa."),
        ("Pemulihan dan ciptaan baru", "Yesaya 65:17-25; 66:22-23", "Tuhan menjanjikan pemulihan, sukacita, damai, dan langit serta bumi yang baru.", "Yerusalem dan ciptaan", "Menjadi bagian dari pengharapan akhir; bandingkan Wahyu 21-22. Ini bukan sekadar peristiwa yang sudah selesai di zaman Yesaya."),
    ],
    "Yeremia": [
        ("Babel dan pembuangan", "Yeremia 25:8-12; 29:10", "Yehuda akan berada di bawah Babel dan menjalani masa pembuangan sebelum Tuhan memulihkan mereka.", "Yerusalem/Yehuda → Babel", "Yerusalem jatuh kepada Babel pada 586 SM; Ezra-Nehemia kemudian mencatat kembalinya sebagian umat."),
        ("Pemulihan setelah 70 tahun", "Yeremia 29:10-14", "Setelah masa yang ditentukan, Tuhan berjanji membawa umat kembali dan mendengar mereka ketika mencari-Nya.", "Babel → Yehuda", "Kepulangan dari pembuangan menjadi latar penggenapan historis janji pemulihan ini."),
        ("Perjanjian baru", "Yeremia 31:31-34", "Tuhan menjanjikan perjanjian baru: hukum-Nya ditulis dalam hati dan dosa diampuni.", "Israel dan Yehuda", "Ibrani 8:8-12 dan 10:16-17 secara langsung mengutip bagian ini dan mengaitkannya dengan karya Kristus."),
        ("Tunas yang benar bagi Daud", "Yeremia 23:5-6; 33:14-18", "Tuhan menjanjikan seorang raja keturunan Daud yang memerintah dengan adil.", "Yehuda/Yerusalem", "PB menempatkan Yesus dalam garis Daud; hubungan ini dibaca bersama silsilah Matius 1 dan Lukas 3."),
    ],
    "Ratapan": [
        ("Kehancuran Yerusalem dan harapan", "Ratapan 1-2; 3:21-26", "Kitab meratapi kehancuran Yerusalem, tetapi di tengah tangisan muncul pengakuan bahwa kasih setia Tuhan tidak berakhir.", "Yerusalem", "Konteks historisnya adalah jatuhnya Yerusalem kepada Babel. Ratapan bukan kitab nubuat Mesianik seperti Yesaya, melainkan puisi ratapan dan pengharapan."),
        ("Pemulihan umat", "Ratapan 5:19-22", "Doa penutup meminta Tuhan mengingat umat dan memulihkan mereka.", "Yerusalem/Yehuda", "Berhubungan dengan harapan pemulihan pascapembuangan, tetapi kitab tidak memberikan jadwal penggenapan tertentu."),
    ],
    "Yehezkiel": [
        ("Hati dan roh yang baru", "Yehezkiel 36:24-28", "Tuhan berjanji mengumpulkan Israel, mentahirkan mereka, dan memberi hati baru serta roh yang baru.", "Israel/Yehuda setelah pembuangan", "Menjadi dasar tema pembaruan umat. Hubungan dengan karya Roh dalam PB dibahas dalam berbagai tradisi teologi, tetapi konteks langsungnya adalah pemulihan Israel."),
        ("Tulang-tulang kering", "Yehezkiel 37:1-14", "Lembah tulang kering menggambarkan umat yang merasa harapannya lenyap, lalu Tuhan menghidupkan kembali harapan mereka.", "Lembah penglihatan Yehezkiel", "Teks sendiri menjelaskan simbol itu sebagai pemulihan Israel dari keadaan terbuang."),
        ("Israel dan Yehuda menjadi satu", "Yehezkiel 37:15-28", "Dua tongkat menjadi satu: umat yang terpecah akan dipersatukan di bawah satu raja/gembala.", "Tanah Israel", "Janji ini berkaitan dengan pemulihan dan kesatuan umat; pembacaan eskatologisnya beragam."),
        ("Gog dan penghakiman", "Yehezkiel 38-39", "Gog memimpin kekuatan besar melawan umat, tetapi Tuhan sendiri menghakimi mereka.", "Pegunungan Israel dalam visi", "Sering dibaca secara eskatologis; identitas dan waktu Gog tidak dinyatakan secara sederhana sebagai satu peristiwa sejarah yang sudah pasti."),
        ("Bait dan tanah yang dipulihkan", "Yehezkiel 40-48", "Penglihatan akhir menggambarkan Bait Allah, pelayanan kudus, sungai, pembagian tanah, dan kehadiran Tuhan.", "Penglihatan tentang tanah Israel", "Menjadi sumber berbagai penafsiran mengenai pemulihan dan zaman akhir; tidak boleh dipaksakan pada satu skema saja."),
    ],
    "Daniel": [
        ("Kerajaan-kerajaan dunia", "Daniel 2:31-45", "Patung dalam mimpi Nebukadnezar melambangkan rangkaian kerajaan, lalu kerajaan Tuhan yang tidak akan binasa.", "Babel; penglihatan kerajaan", "Kisah menekankan bahwa kuasa manusia bersifat sementara sedangkan kerajaan Tuhan kekal. Identifikasi tiap kerajaan ditafsirkan berbeda."),
        ("Anak Manusia menerima kerajaan", "Daniel 7:9-14", "Sosok seperti Anak Manusia datang kepada Yang Lanjut Usianya dan menerima kuasa serta kerajaan kekal.", "Ruang penglihatan Daniel", "Yesus memakai gelar Anak Manusia; Matius 26:64 menggemakan Daniel 7:13-14."),
        ("Masa kesesakan dan kemenangan Tuhan", "Daniel 7:15-28; 12:1", "Setelah masa penindasan dan kesesakan, kuasa atas kerajaan diberikan kepada umat orang-orang kudus Yang Mahatinggi.", "Dalam penglihatan Daniel", "Bagian ini memiliki banyak pembacaan historis dan eskatologis; waktunya tidak boleh dinyatakan secara spekulatif."),
        ("Kebangkitan", "Daniel 12:2-3", "Banyak orang yang tidur dalam debu akan bangun: sebagian kepada hidup kekal dan sebagian kepada kehinaan kekal.", "Masa depan umat", "Menjadi teks penting bagi pengharapan kebangkitan; tema ini juga jelas dalam Yohanes 5:28-29 dan ajaran PB."),
    ],
    "Hosea": [
        ("Anak-anak sebagai tanda", "Hosea 1:4-9", "Nama Yizreel, Lo-Ruhama, dan Lo-Ami menjadi tanda tentang penghukuman dan hubungan perjanjian Israel.", "Kerajaan Israel/Efraim", "Peristiwa keluarga Hosea sendiri menjadi simbol pesan Tuhan kepada Israel."),
        ("Penghakiman atas Israel", "Hosea 4-10", "Israel akan menuai akibat penyembahan berhala, ketidakadilan, dan ketidaksetiaan.", "Samaria/Israel Utara", "Kerajaan Israel Utara akhirnya jatuh kepada Asyur pada 722 SM, sesuai konteks ancaman yang ada dalam periode Hosea."),
        ("Kasih Tuhan dan pemulihan", "Hosea 11:1-11; 14:2-9", "Walau Israel menyimpang, Tuhan tetap memanggilnya pulang dan membuka jalan pemulihan.", "Israel", "Matius 2:15 mengutip Hosea 11:1 dalam kisah Yesus kembali dari Mesir; konteks asli Hosea adalah Israel, sehingga Matius memakai pembacaan tipologis."),
    ],
    "Yoel": [
        ("Hari Tuhan", "Yoel 1:15; 2:1-17", "Bencana dan seruan pertobatan menunjuk pada Hari Tuhan sebagai waktu penghakiman.", "Yehuda/Yerusalem", "Kitab mengajak umat berbalik kepada Tuhan, bukan sekadar menebak tanggal akhir zaman."),
        ("Pemulihan", "Yoel 2:18-27", "Setelah pertobatan, Tuhan menjanjikan pemulihan hasil tanah dan menghapus aib umat.", "Tanah Yehuda", "Janji pemulihan terkait langsung dengan umat yang bertobat dan pemulihan kehidupan mereka."),
        ("Pencurahan Roh", "Yoel 2:28-29", "Roh Tuhan dicurahkan atas anak laki-laki dan perempuan, tua dan muda, hamba laki-laki dan perempuan.", "Umat Tuhan", "Kisah Para Rasul 2:16-21 secara eksplisit menghubungkan Pentakosta dengan nubuat Yoel."),
        ("Tanda-tanda dan keselamatan", "Yoel 2:30-32", "Tanda-tanda kosmis menyertai Hari Tuhan; siapa yang berseru kepada nama Tuhan akan diselamatkan.", "Sion/Yerusalem dan bangsa-bangsa", "Petrus mengutip bagian ini dalam Kisah Para Rasul 2; keselamatan melalui nama Tuhan menjadi tema penting PB."),
    ],
    "Amos": [
        ("Penghakiman Israel", "Amos 2:6-16; 5:1-27", "Israel dihakimi karena penindasan, korupsi, dan ibadah yang tidak disertai keadilan.", "Kerajaan Israel Utara", "Israel Utara kemudian jatuh kepada Asyur pada 722 SM; Amos memperingatkan kehancuran sebelum itu."),
        ("Hari Tuhan bukan kemenangan otomatis", "Amos 5:18-20", "Amos memperingatkan bahwa Hari Tuhan justru akan menjadi kegelapan bagi umat yang hidup dalam dosa.", "Israel", "Pesannya menegaskan bahwa status keagamaan tanpa pertobatan tidak menjamin keselamatan."),
        ("Pondok Daud dipulihkan", "Amos 9:11-15", "Tuhan menjanjikan pemulihan Daud yang roboh dan berkat bagi umat.", "Israel dan bangsa-bangsa", "Kisah Para Rasul 15:15-18 mengutip Amos 9:11-12 dalam pembahasan masuknya bangsa-bangsa ke dalam umat Allah."),
    ],
    "Obaja": [
        ("Edom dihakimi", "Obaja 2-16", "Edom direndahkan karena kesombongan dan tindakannya terhadap Yehuda ketika Yerusalem jatuh.", "Edom dan Yerusalem", "Pesan ini berakar pada permusuhan Edom-Yehuda dan membuka prinsip bahwa kekerasan serta kesombongan akan dihakimi."),
        ("Hari Tuhan atas bangsa-bangsa", "Obaja 15", "Hari Tuhan akan datang atas segala bangsa: apa yang dilakukan akan berbalik kepada pelakunya.", "Bangsa-bangsa", "Horizon penghakiman bersifat luas; kitab tidak memberi tanggal akhir."),
        ("Kerajaan menjadi milik Tuhan", "Obaja 17-21", "Sion dipulihkan dan penutup kitab menyatakan bahwa kerajaan itu milik Tuhan.", "Gunung Sion/Yehuda", "Merupakan pengharapan pemerintahan Tuhan setelah penghakiman."),
    ],
    "Yunus": [
        ("Peringatan kepada Niniwe", "Yunus 1:1-2; 3:4", "Yunus diutus untuk menyampaikan bahwa Niniwe akan menerima hukuman jika tidak bertobat.", "Niniwe, Asyur", "Penduduk Niniwe bertobat dan Tuhan tidak jadi mendatangkan malapetaka yang diberitakan (Yun 3:5-10). Ini menunjukkan bahwa nubuat peringatan dapat berfungsi sebagai panggilan pertobatan."),
        ("Tanda Yunus", "Yunus 1:17; 2:1", "Yunus berada tiga hari tiga malam dalam perut ikan sebelum kembali menjalankan tugasnya.", "Laut dan kemudian Niniwe", "Yesus menyebut tanda Yunus dalam Matius 12:39-41 dan Lukas 11:29-32. Injil memakai kisah Yunus sebagai tanda yang menunjuk kepada kematian dan kebangkitan Yesus."),
    ],
    "Mikha": [
        ("Penghakiman Samaria dan Yerusalem", "Mikha 1-3", "Kota dan pemimpin dihakimi karena penyembahan berhala, korupsi, dan penindasan.", "Samaria dan Yerusalem", "Mikha memperingatkan sebelum kehancuran yang kemudian dialami kerajaan-kerajaan tersebut."),
        ("Bangsa-bangsa belajar jalan Tuhan", "Mikha 4:1-5", "Bangsa-bangsa datang ke gunung rumah Tuhan untuk belajar hukum-Nya dan mengganti perang dengan damai.", "Sion/Yerusalem", "Menjadi gambaran pengharapan damai di bawah pemerintahan Tuhan; penggenapan akhirnya tidak diberi satu tanggal dalam kitab."),
        ("Penguasa dari Betlehem", "Mikha 5:1-4", "Dari Betlehem Efrata akan tampil seorang penguasa yang menggembalakan Israel.", "Betlehem Efrata", "Matius 2:5-6 mengutip Mikha 5 untuk menjelaskan Betlehem dalam kisah kelahiran Yesus."),
        ("Pemulihan sisa umat", "Mikha 7:18-20", "Tuhan mengampuni, menghapus kesalahan, dan tetap setia kepada janji-Nya kepada Abraham dan Yakub.", "Israel/Yehuda", "Penutup kitab menempatkan pengharapan pada karakter Tuhan: kasih setia, pengampunan, dan kesetiaan perjanjian."),
    ],
    "Nahum": [
        ("Kejatuhan Niniwe", "Nahum 1-3", "Niniwe, pusat kekuasaan Asyur, akan dihancurkan karena kekerasan dan penindasannya.", "Niniwe, Asyur", "Niniwe jatuh pada 612 SM dalam sejarah kuno; peristiwa itu biasa dipandang selaras dengan pesan Nahum."),
        ("Penghiburan bagi Yehuda", "Nahum 1:7-15", "Tuhan menjadi tempat perlindungan bagi orang yang berharap kepada-Nya dan penindas tidak akan terus berkuasa.", "Yehuda", "Nubuat ini memberi sudut pandang teologis atas runtuhnya penindasan Asyur."),
    ],
    "Habakuk": [
        ("Babel sebagai alat penghakiman", "Habakuk 1:5-11", "Tuhan membangkitkan orang Kasdim/Babel untuk menghukum kejahatan yang sedang merajalela.", "Yehuda dan Babel", "Bangkitnya Babel menjadi kenyataan politik besar pada akhir abad ke-7 SM."),
        ("Babel juga akan dihakimi", "Habakuk 2:6-20", "Orang yang menjarah, menumpahkan darah, dan membangun kekuasaan dengan kesombongan akan menerima celaka.", "Bangsa-bangsa/Babel", "Pesannya menegaskan bahwa Tuhan tidak membenarkan alat penghakiman secara mutlak; Babel juga bertanggung jawab atas dosanya."),
        ("Orang benar hidup oleh iman", "Habakuk 2:4", "Di tengah penantian, orang benar dipanggil untuk hidup dalam iman/kesetiaan kepada Tuhan.", "Komunitas umat Tuhan", "Roma 1:17, Galatia 3:11, dan Ibrani 10:38 mengutip Habakuk 2:4 sebagai teks penting dalam PB."),
    ],
    "Zefanya": [
        ("Hari Tuhan", "Zefanya 1:14-18", "Hari Tuhan digambarkan sebagai hari murka dan penghakiman terhadap dosa.", "Yehuda dan bangsa-bangsa", "Pesannya lahir dalam konteks reformasi Yosia, tetapi gambaran Hari Tuhan memiliki horizon lebih luas."),
        ("Sisa umat yang rendah hati", "Zefanya 3:11-13", "Setelah penghakiman, Tuhan menyisakan umat yang rendah hati dan berlindung kepada-Nya.", "Yerusalem", "Ini menjadi pola pengharapan: penghakiman tidak menjadi kata terakhir bagi umat yang kembali kepada Tuhan."),
        ("Tuhan memulihkan dan bersukacita", "Zefanya 3:14-20", "Tuhan mengumpulkan umat, memulihkan nama mereka, dan digambarkan bersukacita atas mereka.", "Sion/Yerusalem", "Merupakan janji pemulihan; waktu dan bentuk penggenapan akhirnya tidak ditetapkan secara eksplisit."),
    ],
    "Hagai": [
        ("Pembangunan kembali Bait Allah", "Hagai 1:2-11", "Umat ditegur karena sibuk dengan rumah sendiri sementara rumah Tuhan terbengkalai.", "Yerusalem, Yehuda", "Zerubabel dan Yosua kemudian memimpin pembangunan kembali Bait Allah."),
        ("Kemuliaan rumah yang baru", "Hagai 2:6-9", "Tuhan akan menggoncangkan bangsa-bangsa dan menjanjikan kemuliaan yang lebih besar bagi rumah ini.", "Yerusalem", "Hagai 2:6 dikutip dalam Ibrani 12:26 sebagai gambaran goncangan ciptaan dan kerajaan yang tidak tergoncangkan; penerapan keseluruhan bagian dipahami beragam."),
        ("Zerubabel sebagai cincin meterai", "Hagai 2:20-23", "Zerubabel diteguhkan sebagai hamba pilihan Tuhan di tengah pemulihan pascapembuangan.", "Yerusalem/Yehuda", "Menegaskan harapan atas garis kepemimpinan Daud, tetapi kitab tidak mengatakan bahwa Zerubabel menjadi raja yang memerintah sebagai kerajaan mandiri."),
    ],
    "Zakharia": [
        ("Pemulihan Yerusalem", "Zakharia 1-2", "Tuhan berjanji kembali kepada Yerusalem dan memperluas perlindungan serta pemulihan kota.", "Yerusalem", "Terjadi dalam konteks komunitas pascapembuangan yang sedang membangun kembali kota dan Bait Allah."),
        ("Yosua imam besar dibersihkan", "Zakharia 3", "Yosua berdiri sebagai imam besar dengan pakaian kotor, lalu Tuhan membersihkannya dan menyingkirkan kesalahannya.", "Yerusalem/Bait Allah", "Menjadi gambaran pemulihan jabatan imam dan umat; teks tidak menyamakan Yosua ini dengan Yesus dalam identitas historis."),
        ("Raja yang rendah hati", "Zakharia 9:9-10", "Raja datang ke Sion dengan rendah hati, menunggang keledai, dan membawa damai kepada bangsa-bangsa.", "Sion/Yerusalem", "Matius 21:4-5 dan Yohanes 12:14-15 menghubungkannya dengan masuknya Yesus ke Yerusalem."),
        ("Gembala dipukul", "Zakharia 13:7", "Pedang menyerang gembala dan domba-domba tercerai-berai.", "Bahasa nubuat; konteks umat Tuhan", "Matius 26:31 dan Markus 14:27 mengutipnya ketika Yesus berbicara tentang para murid yang tercerai-berai."),
        ("Hari Tuhan dan pemerintahan-Nya", "Zakharia 12-14", "Yerusalem menghadapi konflik, tetapi penutup kitab menampilkan Tuhan sebagai Raja atas seluruh bumi.", "Yerusalem", "Banyak bagian dibaca secara eskatologis dan dikaitkan dengan pengharapan akhir; penafsiran detailnya beragam."),
    ],
    "Maleakhi": [
        ("Utusan mempersiapkan jalan", "Maleakhi 3:1", "Seorang utusan datang mendahului Tuhan yang datang ke bait-Nya.", "Bait Allah/Yerusalem", "Matius 11:10, Markus 1:2, dan Lukas 7:27 menghubungkan gambaran utusan dengan Yohanes Pembaptis."),
        ("Tuhan datang untuk memurnikan", "Maleakhi 3:2-5", "Tuhan digambarkan seperti api pemurni dan sabun penatu, menghakimi dosa dan memurnikan umat.", "Yerusalem/Bait Allah", "Tema pemurnian menjadi bagian dari pengharapan kedatangan Tuhan; PB mengaitkan pelayanan Yohanes dengan persiapan jalan, tetapi tidak menyamakan semua detail secara satu-banding-satu."),
        ("Elia sebelum Hari Tuhan", "Maleakhi 4:5-6", "Elia akan datang sebelum Hari Tuhan yang besar dan dahsyat untuk membalikkan hati.", "Umat Tuhan", "Lukas 1:17 menggambarkan Yohanes Pembaptis datang dalam roh dan kuasa Elia; ini menjelaskan hubungan tipologis/fungsional, bukan bahwa Yohanes adalah Elia yang kembali secara literal."),
    ],
}


def character_screen(book):
    """TOKOH hanya berisi nabi/tokoh kenabian utama, lengkap dengan nubuatan."""
    prophet_names = {
        'Yesaya': 'Yesaya', 'Yeremia': 'Yeremia',
        # Ratapan tidak menyebut penulis; tradisi kuno sering mengaitkannya dengan Yeremia.
        'Ratapan': 'Yeremia (tradisi)',
        'Yehezkiel': 'Yehezkiel', 'Daniel': 'Daniel', 'Hosea': 'Hosea',
        'Yoel': 'Yoel', 'Amos': 'Amos', 'Obaja': 'Obaja', 'Yunus': 'Yunus',
        'Mikha': 'Mikha', 'Nahum': 'Nahum', 'Habakuk': 'Habakuk',
        'Zefanya': 'Zefanya', 'Hagai': 'Hagai', 'Zakharia': 'Zakharia',
        'Maleakhi': 'Maleakhi'
    }
    prophet = prophet_names.get(book)
    idx = [b[0] for b in BOOKS].index(book) + 1
    if book == 'Ratapan':
        prophet = 'Yeremia (tradisi)'
        sections = [
            ('STATUS PENULIS', 'Ratapan tidak menyebut nama penulis secara eksplisit. Tradisi Yahudi dan Kristen kuno sering mengaitkannya dengan Yeremia, tetapi hal itu tidak dapat dipastikan hanya dari teks kitab.'),
            ('KISAHNYA', 'Kitab ini meratap atas kehancuran Yerusalem. Di tengah luka, penulis mengingat bahwa kasih setia Tuhan tidak berakhir dan masih ada alasan untuk berharap.'),
            ('NUBUATAN / PENGHARAPAN', 'Ratapan terutama merupakan puisi ratapan, bukan kitab nubuat seperti Yesaya atau Yeremia. Pengharapannya terletak pada belas kasihan, kesetiaan, dan pemulihan Tuhan.'),
            ('AYAT', 'Ratapan 3:21-26; 5:19-22'),
            ('KONTEKS / DIMANA', 'Yerusalem sesudah kehancuran kota dan Bait Allah oleh Babel.'),
            ('KAITAN', 'Ratapan memberi kesaksian iman di tengah penghakiman dan kehancuran; bukan setiap gambaran dalam kitab ini merupakan nubuat mesianik yang memiliki penggenapan langsung dalam Perjanjian Baru.')
        ]
    else:
        desc = CHARACTER_GUIDE.get(book, {}).get(prophet, '')
        story_intro = {'Yesaya': 'Yesaya dipanggil di Yerusalem dan melayani pada masa Uzia, Yotam, Ahas, dan Hizkia. Ia menegur Yehuda, menghadapi krisis Aram-Israel dan Asyur, memperingatkan pembuangan, lalu membawa pengharapan tentang Raja, Hamba Tuhan, keselamatan bangsa-bangsa, dan pemulihan.', 'Yeremia': 'Yeremia dipanggil ketika Yehuda menuju kehancuran. Ia menghadapi raja, imam, penolakan dan pembuangan, tetapi tetap menyampaikan janji pemulihan dan perjanjian baru yang ditulis dalam hati.', 'Yehezkiel': 'Yehezkiel melayani di tengah pembuangan Babel. Penglihatannya menjelaskan penghakiman atas Yerusalem sekaligus membawa janji hati baru, pemulihan Israel, kesatuan umat, dan kehadiran Tuhan.', 'Daniel': 'Daniel hidup di tengah kekuasaan Babel dan Persia. Kesetiaannya kepada Tuhan berjalan bersama penglihatan tentang kerajaan dunia, Anak Manusia, kesesakan, kemenangan umat Tuhan, dan kebangkitan.', 'Hosea': 'Hosea memakai kehidupan keluarganya sebagai tanda profetis bagi Israel. Ketidaksetiaan keluarganya menggambarkan ketidaksetiaan Israel, tetapi kasih Tuhan terus memanggil umat untuk kembali dan dipulihkan.', 'Yoel': 'Yoel berangkat dari bencana belalang menuju seruan pertobatan. Ia berbicara tentang Hari Tuhan, pemulihan tanah, pencurahan Roh, tanda-tanda, dan keselamatan.', 'Amos': 'Amos dari Tekoa diutus kepada Israel utara. Ia menegur kemakmuran yang dibangun di atas penindasan dan menegaskan bahwa ibadah harus berjalan bersama keadilan.', 'Obaja': 'Obaja mengumumkan penghakiman atas Edom karena kesombongan dan tindakannya terhadap Yehuda, lalu mengarah pada Hari Tuhan atas bangsa-bangsa dan kerajaan Tuhan.', 'Yunus': 'Yunus diutus ke Niniwe, melarikan diri, diselamatkan Tuhan, lalu kembali menjalankan tugas. Pertobatan Niniwe memperlihatkan keluasan belas kasihan Tuhan.', 'Mikha': 'Mikha menegur pemimpin yang menindas di Samaria dan Yerusalem. Ia mengumumkan penghakiman sekaligus melihat damai, pemulihan, dan seorang penguasa yang keluar dari Betlehem.', 'Nahum': 'Nahum mengumumkan kejatuhan Niniwe dan Asyur karena kekerasan serta penindasan. Bagi Yehuda, berita ini juga menjadi penghiburan bahwa penindas tidak berkuasa selamanya.', 'Habakuk': 'Habakuk membawa pertanyaan tentang kejahatan kepada Tuhan. Ia diberi tahu bahwa Babel akan menjadi alat penghakiman, tetapi Babel juga akan dihakimi. Nabi akhirnya belajar menanti dengan iman.', 'Zefanya': 'Zefanya berbicara tentang Hari Tuhan yang menghakimi Yehuda dan bangsa-bangsa, tetapi juga tentang sisa umat yang rendah hati dan pemulihan Yerusalem.', 'Hagai': 'Hagai menegur komunitas pascapembuangan karena Bait Allah terbengkalai. Ia mendorong pembangunan kembali dan menyampaikan janji tentang kemuliaan serta pengharapan.', 'Zakharia': 'Zakharia melayani komunitas pascapembuangan melalui penglihatan-penglihatan simbolis. Ia berbicara tentang pemulihan Yerusalem, imam yang dibersihkan, Raja yang rendah hati, Gembala, dan pemerintahan Tuhan.', 'Maleakhi': 'Maleakhi menegur imam dan umat setelah pembuangan karena ibadah yang tidak sungguh-sungguh. Ia mengarahkan pandangan kepada utusan, pemurnian, dan Hari Tuhan.'}.get(prophet, "")
        sections = [("SIAPA DIA", desc), ("KISAHNYA", story_intro)]
        for title, refs, event, where, connection in PROPHECY_DETAIL.get(book, []):
            sections += [("NUBUATAN", title), ("AYAT", refs), ("KEJADIAN / KONTEKS", event), ("DIMANA", where), ("PENGGENAPAN / KAITAN", connection)]
    viewport = pygame.Rect(55, 138, 1170, 510)
    card_x, card_w = viewport.x + 12, viewport.w - 32
    inner_w = card_w - 56
    prepared=[]
    for label, txt in sections:
        prepared.append((label, wrap_text(str(txt), SMALL, inner_w) or [""]))
    card_h = 78
    for label, ls in prepared: card_h += 35 + len(ls)*21 + 10
    max_scroll=max(0, card_h-viewport.h+24)
    scroll=0
    while True:
        draw_background(); header(book, "NABI UTAMA · NUBUATAN · PENGGENAPAN", idx)
        scroll=max(0,min(scroll,max_scroll))
        old=screen.get_clip(); screen.set_clip(viewport); screen.fill(SURFACE, viewport)
        r=pygame.Rect(card_x, int(viewport.y+12-scroll), card_w, card_h); card(r,SURFACE_2)
        inner=pygame.Rect(r.x+28,r.y+20,r.w-56,r.h-40); screen.set_clip(inner.clip(viewport))
        text_blit(prophet,inner.x,inner.y,BIG,IVORY,inner.w); ty=inner.y+44
        for label, ls in prepared:
            text_blit(label,inner.x,ty,SMALL,GOLD,inner.w); ty+=23
            for line in ls: text_blit(line,inner.x,ty,SMALL,IVORY if label=="NUBUATAN" else MUTED,inner.w); ty+=21
            ty+=10
        screen.set_clip(old); pygame.draw.rect(screen,LINE,viewport,1,border_radius=12)
        if max_scroll>0:
            track=pygame.Rect(viewport.right-10,viewport.y+10,5,viewport.h-20); pygame.draw.rect(screen,LINE,track,border_radius=3); thumb_h=max(55,int(track.h*viewport.h/max(card_h,viewport.h))); thumb_y=track.y+int((track.h-thumb_h)*scroll/max_scroll); pygame.draw.rect(screen,GOLD_SOFT,pygame.Rect(track.x,thumb_y,track.w,thumb_h),border_radius=3)
        button((55,665,135,44),"KEMBALI"); button((210,665,190,44),"ENSIKLOPEDIA",True); button((1070,665,155,44),"ATAS",True); pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT: quit_game()
            elif e.type==pygame.KEYDOWN:
                if e.key==pygame.K_ESCAPE: return
                elif e.key==pygame.K_DOWN: scroll=min(max_scroll,scroll+50)
                elif e.key==pygame.K_UP: scroll=max(0,scroll-50)
                elif e.key==pygame.K_PAGEDOWN: scroll=min(max_scroll,scroll+viewport.h-70)
                elif e.key==pygame.K_PAGEUP: scroll=max(0,scroll-viewport.h+70)
                elif e.key==pygame.K_HOME: scroll=0
                elif e.key==pygame.K_END: scroll=max_scroll
            elif e.type==pygame.MOUSEWHEEL: scroll=max(0,min(max_scroll,scroll-e.y*50))
            elif e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
                p=e.pos
                if pygame.Rect(55,665,135,44).collidepoint(p): return
                elif pygame.Rect(210,665,190,44).collidepoint(p): open_encyclopedia(prophet if prophet else book)
                elif pygame.Rect(1070,665,155,44).collidepoint(p): scroll=0

def select_book():
    selected = 0
    while True:
        draw_background()
        header("PERJALANAN", "Pilih Kitab", None)
        # Semua pilihan memakai Rect yang sama untuk gambar dan klik, sehingga
        # posisi visual dan area klik tidak pernah bergeser.
        cols = 2
        rows = 9
        gap_x, gap_y = 28, 12
        x0, y0 = 70, 150
        card_w, card_h = 545, 49
        rects = []
        for i, (name, *_rest) in enumerate(BOOKS):
            col = i // rows
            row = i % rows
            r = pygame.Rect(x0 + col * (card_w + gap_x), y0 + row * (card_h + gap_y), card_w, card_h)
            rects.append(r)
            active = i == selected
            card(r, SURFACE_2 if active else SURFACE)
            pygame.draw.rect(screen, GOLD_SOFT if active else LINE, r, 1, border_radius=10)
            text_blit(f"{i+1:02d}", r.x + 18, r.y + 14, SMALL, GOLD if active else MUTED)
            text_blit(name, r.x + 70, r.y + 12, FONT, IVORY if active else MUTED, r.w - 90)

        button((70, 665, 130, 44), "KEMBALI")
        button((1070, 665, 140, 44), "BUKA", True)
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit_game()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    return
                elif e.key in (pygame.K_UP, pygame.K_w) and selected % rows > 0:
                    selected -= 1
                elif e.key in (pygame.K_DOWN, pygame.K_s) and selected % rows < rows - 1 and selected + 1 < len(BOOKS):
                    selected += 1
                elif e.key in (pygame.K_LEFT, pygame.K_a) and selected >= rows:
                    selected -= rows
                elif e.key in (pygame.K_RIGHT, pygame.K_d) and selected + rows < len(BOOKS):
                    selected += rows
                elif e.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    return book_menu(BOOKS[selected][0])
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                p = e.pos
                for i, r in enumerate(rects):
                    if r.collidepoint(p):
                        selected = i
                        return book_menu(BOOKS[i][0])
                if pygame.Rect(70, 665, 130, 44).collidepoint(p):
                    return
                if pygame.Rect(1070, 665, 140, 44).collidepoint(p):
                    return book_menu(BOOKS[selected][0])

def book_menu(book):
    """Menu khusus setiap kitab: semua pintu utama terlihat sebelum masuk cerita."""
    idx = [b[0] for b in BOOKS].index(book) + 1
    meta = next(b for b in BOOKS if b[0] == book)
    while True:
        draw_background()
        header(book, "Perjalanan Kitab", idx)
        card((70,145,1140,150), SURFACE)
        text_blit(meta[1], 105, 178, BIG, IVORY, 1040)
        text_blit(meta[2], 105, 220, SMALL, MUTED, 1040)
        text_blit(meta[3], 105, 248, SMALL, MUTED, 1040)

        # Lima pintu utama dibuat jelas dan konsisten.
        buttons = [
            (70,350,330,58,"MULAI CERITA"),
            (425,350,330,58,"TOKOH & NUBUATAN"),
            (850,350,330,58,"ALKITAB"),
            (70,435,330,58,"STUDI"),
            (425,435,330,58,"ENSIKLOPEDIA"),
            (850,435,330,58,"AYAT PENTING"),
        ]
        for x,y,w,h,label in buttons:
            button((x,y,w,h), label, label in ("MULAI CERITA","TOKOH & NUBUATAN"))
        button((70,665,150,44),"PILIH KITAB")
        button((1070,665,140,44),"KEMBALI",True)
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit_game()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    return
                if e.key == pygame.K_RETURN:
                    return story_screen(book, 0)
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                p=e.pos
                if pygame.Rect(70,350,330,58).collidepoint(p):
                    return story_screen(book,0)
                if pygame.Rect(425,350,330,58).collidepoint(p):
                    character_screen(book)
                elif pygame.Rect(850,350,330,58).collidepoint(p):
                    open_bible(book)
                elif pygame.Rect(70,435,330,58).collidepoint(p):
                    open_study(book)
                elif pygame.Rect(425,435,330,58).collidepoint(p):
                    open_encyclopedia(book)
                elif pygame.Rect(850,435,330,58).collidepoint(p):
                    verse_reader(book)
                elif pygame.Rect(70,665,150,44).collidepoint(p):
                    return select_book()
                elif pygame.Rect(1070,665,140,44).collidepoint(p):
                    return

def main_menu():
    while True:
        draw_background()
        text_blit("THE GREAT JOURNEY",70,125,TITLE,IVORY)
        text_blit("17 KITAB  ·  YESAYA — MALEAKHI",74,195,SMALL,GOLD)
        pygame.draw.line(screen,GOLD_SOFT,(74,235),(330,235),2)
        text_blit("Sebuah perjalanan melalui kisah, tokoh, ayat,",74,285,BODY,MUTED)
        text_blit("dan suara para nabi.",74,318,BODY,MUTED)
        card((760,105,420,420),SURFACE)
        text_blit("PERJALANAN",800,150,SMALL,GOLD)
        for i,(name,*_) in enumerate(BOOKS):
            text_blit(f"{i+1:02d}",800,190+i*18,SMALL,GOLD_SOFT)
            text_blit(name,845,190+i*18,SMALL,IVORY)
        button((74,585,190,52),"MULAI",True)
        button((280,585,190,52),"ALKITAB")
        button((486,585,190,52),"KELUAR")
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT:quit_game()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_RETURN:select_book()
                if e.key==pygame.K_ESCAPE:quit_game()
            if e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
                p=e.pos
                if pygame.Rect(74,585,190,52).collidepoint(p):select_book()
                elif pygame.Rect(280,585,190,52).collidepoint(p):bible_screen()
                elif pygame.Rect(486,585,190,52).collidepoint(p):quit_game()

def bible_screen():
    book="Yesaya"; chapter=1
    while True:
        draw_background(); header("ALKITAB","Baca",None)
        text_blit("Pilih kitab dan pasal.",70,155,BODY,IVORY)
        card((70,205,1140,330),SURFACE)
        text_blit(book,105,240,BIG,IVORY); text_blit(f"Pasal {chapter}",105,290,SMALL,GOLD)
        text_blit("Teks lengkap dibuka di Alkitab online.",105,335,SMALL,MUTED)
        button((105,445,170,48),"BACA ALKITAB",True); button((295,445,170,48),"STUDI")
        button((70,665,130,44),"KEMBALI")
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT:quit_game()
            if e.type==pygame.KEYDOWN and e.key==pygame.K_ESCAPE:return
            if e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
                p=e.pos
                if pygame.Rect(105,445,170,48).collidepoint(p):open_bible(book,chapter)
                elif pygame.Rect(295,445,170,48).collidepoint(p):open_study(book)
                elif pygame.Rect(70,665,130,44).collidepoint(p):return

def quiz_screen():
    i=0
    while True:
        book,q,a=QUESTION_BANK[i]
        draw_background(); header("KISI-KISI",book,[b[0] for b in BOOKS].index(book)+1)
        card((70,160,1140,300),SURFACE)
        text_blit("PERTANYAAN",105,195,SMALL,GOLD)
        for j,line in enumerate(wrap_text(q,BODY,1030)[:6]):text_blit(line,105,235+j*31,BODY,IVORY)
        card((70,485,1140,105),SURFACE_2)
        text_blit("KUNCI",105,510,SMALL,GOLD)
        for j,line in enumerate(wrap_text(a,SMALL,1030)[:2]):text_blit(line,105,540+j*21,SMALL,MUTED)
        button((70,665,130,44),"KEMBALI");button((1070,665,140,44),"LANJUT",True)
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT:quit_game()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_ESCAPE:return
                if e.key==pygame.K_RIGHT and i<len(QUESTION_BANK)-1:i+=1
            if e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
                p=e.pos
                if pygame.Rect(70,665,130,44).collidepoint(p):return
                if pygame.Rect(1070,665,140,44).collidepoint(p) and i<len(QUESTION_BANK)-1:i+=1

def metadata_screen(book):
    after_story_screen(book)

def verse_reader(book):
    verses=VERSE_DATA[book]
    while True:
        draw_background();header(book,"Ayat",[b[0] for b in BOOKS].index(book)+1)
        for i,(ref,meaning) in enumerate(verses[:6]):
            r=pygame.Rect(70,150+i*82,1140,65);card(r,SURFACE)
            text_blit(ref,95,r.y+13,FONT,IVORY);text_blit(meaning,300,r.y+16,SMALL,MUTED)
        button((70,665,130,44),"KEMBALI")
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT:quit_game()
            if e.type==pygame.KEYDOWN and e.key==pygame.K_ESCAPE:return
            if e.type==pygame.MOUSEBUTTONDOWN and e.button==1 and pygame.Rect(70,665,130,44).collidepoint(e.pos):return

def bible_reader(book, chapter):
    open_bible(book,chapter)

def quit_game():
    pygame.quit();sys.exit()

def main():
    main_menu()

if __name__ == "__main__":
    main()
