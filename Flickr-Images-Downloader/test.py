import time, subprocess
import scraper
import threading
import multiprocessing
import os
import sys
from datetime import datetime, timedelta

plants = ['"Abelia chinensis"','"Abeliophyllum distichum"','"Abelmoschus manihot"','"Abelmoschus moschatus"','"Abies homolepis"','"Abies koreana"','"Abies nordmanniana"','"Acanthus mollis"','"Acanthus montanus"','"Acanthus spinosus"','"Acer buergerianum"','"Acer campestre"','"Acer capillipes"','"Acer cappadocicum"','"Acer carpinifolium"','"Acer cissifolium"','"Acer davidii"','"Acer japonicum"','"Acer macrophyllum"','"Acer maximowiczianum"','"Acer miyabei"','"Acer monspessulanum"','"Acer oliverianum"','"Acer pensylvanicum"','"Acer pictum"','"Acer pseudosieboldianum"','"Acer tataricum"','"Acer triflorum"','"Achillea ageratifolia"','"Achillea aegyptiaca"','"Achillea sibirica"','"Aciphylla aurea"','"Blighia sapida"','"Aconitum carmichaelii"','"Aconitum hemsleyanum"','"Aconitum volubile"','"Aconitum napellus"','"Acorus calamus"','"Actaea pachypoda"','"Actaea podocarpa"','"Actaea racemosa"','"Actaea simplex"','"Actinidia deliciosa"','"Actinidia kolomikta"','"Adiantum pedatum"','"Adiantum raddianum"','"Adina rubella"','"Adonidia merrillii"','"Aechmea fasciata"','"Aeschynanthus radicans"','"Aesculus californica"','"Aesculus chinensis"','"Aesculus flava"','"Aesculus glabra"','"Aesculus sylvatica"','"Agalinis tenuifolia"','"Agastache nepetoides"','"Agastache cana"','"Agave schidigera"','"Agave geminiflora"','"Manfreda virginica"','"Ageratina altissima"','"Agrostis palustris"','"Alangium platanifolium"','"Alcea rugosa"','"Aleurites moluccanus"','"Alisma triviale"','"Allium ampeloprasum"','"Allium babingtonii"','"Allium caeruleum"','"Allium cristophii"','"Allium giganteum"','"Allium moly"','"Allium schubertii"','"Allium senescens"','"Allium stellatum"','"Allium ursinum"','"Pimenta dioica"','"Alnus cordata"','"Alnus glutinosa"','"Alnus incana"','"Alnus japonica"','"Alnus maritima"','"Alocasia amazonica"','"Aloysia virgata"','"Aloysia citriodora"','"Alpinia japonica"','"Alpinia galanga"','"Alstroemeria aurea"','"Alstroemeria isabellana"','"Alstroemeria ligtu"','"Alternanthera dentata"','"Alyssum murale"','"Amaranthus caudatus"','"Amelanchier nantucketensis"','"Amelanchier stolonifera"','"Amelanchier arborea"','"Amelanchier obovalis"','"Amelanchier laevis"']


for i in plants:
    os.system('python scraper.py --search '+i+' --max-pages 1 --start-page 1')
    # a = subprocess.Popen('python scraper.py --search '+i+' --original --max-pages 1 --start-page 0', shell=True)
    # time.sleep(10)
    # subprocess.Popen.kill(a)
