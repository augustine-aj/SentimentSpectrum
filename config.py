# Config files

# 1. Xpaths as dictionary values
# 2.


xpaths_details = {
    'Phone_Name': '//div[@class="C7fEHH"]//div/h1',
    'Rating': '//div[@class="_5OesEi HDvrBb"]//div[@class="XQDdHH"]',
    'Discount_Price': '//div[@class="Nx9bqj CxhGGd"]',
    'Discount': '//div[@class="UkUFwK WW8yVX"]',
    'Actual_Price': '//div[@class="yRaY8j A6+E6v"]',
    'Warranty': '//div[@class="zIL+eP"]',
    'Storage': '//div[@class="WGBwfw"]',
    'Highlights': '//div[@class="xFVion"]',
    'Seller_Name': '//div[@id="sellerName"]/span/span',
    'Seller_Rating': '//div[@class="XQDdHH uuhqql"]',
    'Total_Rating': '//div[contains(@class, "j-aW8Z")]/div/span[contains(text(), "Ratings")]',
    'Total_Review': '//div[contains(@class, "j-aW8Z")]/div/span[contains(text(), "Reviews")]',
    'Rating_5Star-1Star': '//ul[@class="+psZUR"]',
    'Total_Reviews': '//div[@class="_23J90q RcXBOT"]/span',
}

xpaths_review = {
    'Rating': '//div[@class="XQDdHH Ga3i8K"]',
    'Review_Title': '//div/p[@class="z9E0IG"]',
    'Review': '//div[@class="ZmyHeo"]',
    'Reviewer_Name': '//div/p[@class="_2NsDsF AwS1CA"]',
    'Reviewer_Location': '//div/p[@class="MztJPv"]/span[2]',
    'Review_Date': '//div/p[@class="_2NsDsF"]',
    'Review_Likes': '//div[@class="_6kK6mk"]/span[@class="tl9VpF"]',
    'Review_Dislikes': '//div[@class="_6kK6mk aQymJL"]/span[@class="tl9VpF"]',
}

cameraRating = {
    'Camera_Rating': '//div[@class="tobygM"]',
    'Camera_Positive_Feedback': '//div[@class="SmC0g8"]//div[1]/span[@class="WtBCuZ"]',
    'Camera_Negative_Feedback': '//div[@class="SmC0g8"]//div[2]/span[@class="_9VjbDx"]',
}

cameraReview = {
    'Camera_Review_Title': '//div/p[@class="z9E0IG"]',
    'Camera_Review': '//div[@class="ZmyHeo"]',
    'Camera_Reviewer_Name': '//div/p[@class="_2NsDsF AwS1CA"]',
    'Camera_Reviewer_Location': '//div/p[@class="MztJPv"]/span[2]',
    'Camera_Review_Date': '//div/p[@class="_2NsDsF"]',
    'Camera_review_Likes': '//div[@class="_6kK6mk"]/span[@class="tl9VpF"]',
    'Camera_Review_Dislikes': '//div[@class="_6kK6mk aQymJL"]/span[@class="tl9VpF"]',
}

batteryRating = {
    'Battery_Rating': '//div[@class="tobygM"]',
    'Battery_Positive_Feedback': '//div[@class="SmC0g8"]//div[1]/span[@class="WtBCuZ"]',
    'Battery_Negative_Feedback': '//div[@class="SmC0g8"]//div[2]/span[@class="_9VjbDx"]',
}

batteryReview = {
    'Battery_Review_Title': '//div/p[@class="z9E0IG"]',
    'Battery_Review': '//div[@class="ZmyHeo"]',
    'Battery_Reviewer_Name': '//div/p[@class="_2NsDsF AwS1CA"]',
    'Battery_Reviewer_Location': '//div/p[@class="MztJPv"]/span[2]',
    'Battery_Review_Date': '//div/p[@class="_2NsDsF"]',
    'Battery_Review_Likes': '//div[@class="_6kK6mk"]/span[@class="tl9VpF"]',
    'Battery_Review_Dislikes': '//div[@class="_6kK6mk aQymJL"]/span[@class="tl9VpF"]',
}
displayRating = {
    'Display_Rating': '//div[@class="tobygM"]',
    'Display_Positive_Feedback': '//div[@class="SmC0g8"]//div[1]/span[@class="WtBCuZ"]',
    'Display_Negative_Feedback': '//div[@class="SmC0g8"]//div[2]/span[@class="_9VjbDx"]',
}

displayReview = {
    'Display_Review_Title': '//div/p[@class="z9E0IG"]',
    'Display_Review': '//div[@class="ZmyHeo"]',
    'Display_Reviewer_Name': '//div/p[@class="_2NsDsF AwS1CA"]',
    'Display_Reviewer_Location': '//div/p[@class="MztJPv"]/span[2]',
    'Display_Review_Date': '//div/p[@class="_2NsDsF"]',
    'Display_Review_Likes': '//div[@class="_6kK6mk"]/span[@class="tl9VpF"]',
    'Display_Review_Dislikes': '//div[@class="_6kK6mk aQymJL"]/span[@class="tl9VpF"]',
}

performanceRating = {
    'Performance_Rating': '//div[@class="tobygM"]',
    'Performance_Positive_Feedback': '//div[@class="SmC0g8"]//div[1]/span[@class="WtBCuZ"]',
    'Performance_Negative_Feedback': '//div[@class="SmC0g8"]//div[2]/span[@class="_9VjbDx"]',
}

performanceReview = {
    'Performance_Review_Title': '//div/p[@class="z9E0IG"]',
    'Performance_Review': '//div[@class="ZmyHeo"]',
    'Performance_Reviewer_Name': '//div/p[@class="_2NsDsF AwS1CA"]',
    'Performance_Reviewer_Location': '//div/p[@class="MztJPv"]/span[2]',
    'Performance_Review_Date': '//div/p[@class="_2NsDsF"]',
    'Performance_Review_Likes': '//div[@class="_6kK6mk"]/span[@class="tl9VpF"]',
    'Performance_Review_Dislikes': '//div[@class="_6kK6mk aQymJL"]/span[@class="tl9VpF"]',
}

phone_list = {
    'iPhone': {
        'iPhone X': ['https://www.flipkart.com/apple-iphone-x-silver-256-gb/p/itmexrgv4cgmrxxp?pid=MOBEXRGVVTMF9FYV&lid=LSTMOBEXRGVVTMF9FYVKHKOAY&marketplace=FLIPKART&q=iPhone+X&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=b68a925c-faa0-4229-a15f-a061855b1a7c.MOBEXRGVVTMF9FYV.SEARCH&ppt=sp&ppn=sp&ssid=0rmgvi81g00000001723996563730&qH=079a3d134d2387ad', 'apple iphone x silver 256 gb'],
        'iPhone XS': ['https://www.flipkart.com/apple-iphone-xs-silver-512-gb/p/itmf944eevczqk7x?pid=MOBF944EFE7HZWHB&lid=LSTMOBF944EFE7HZWHBTIGVUO&marketplace=FLIPKART&q=iPhone+XS&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=3b75b0be-e717-4789-b9b2-28c7c9c253ef.MOBF944EFE7HZWHB.SEARCH&ppt=sp&ppn=sp&ssid=9qaad514g00000001723996453357&qH=57035d69cca71b58', 'apple iphone xs silver 512 gb'],
        'iPhone XR': ['https://www.flipkart.com/apple-iphone-xr-white-64-gb-includes-earpods-power-adapter/p/itmf9z7zhgzkmgm3?pid=MOBF9Z7ZUYC2EYQD&lid=LSTMOBF9Z7ZUYC2EYQDVYJTIC&marketplace=FLIPKART&q=iPhone+XR&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=ef69c7b9-0dee-4583-b165-90f377adfce4.MOBF9Z7ZUYC2EYQD.SEARCH&ppt=sp&ppn=sp&ssid=lfiw0ovc8g0000001723996788108&qH=55c0edd3941a21ba', 'apple iphone xr white 64 gb includes earpods power adapter'],
        'iPhone 11': ['https://www.flipkart.com/apple-iphone-11-white-128-gb/p/itme32df47ea6742?pid=MOBFWQ6B7KKRXDDS&lid=LSTMOBFWQ6B7KKRXDDSULUZ0N&marketplace=FLIPKART&q=iPhone+11&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=e8d930d8-201e-4750-99e2-5e3b8ba86b60.MOBFWQ6B7KKRXDDS.SEARCH&ppt=sp&ppn=sp&ssid=04gyjpx9o00000001723996879729&qH=ecfeaec4f2c91969', 'apple iphone 11 white 128 gb'],
        'iPhone SE 2': ['https://www.flipkart.com/apple-iphone-se-red-64-gb-includes-earpods-power-adapter/p/itm6e9443811d36a?pid=MOBFRFXHYMPBSB5H&lid=LSTMOBFRFXHYMPBSB5HVHY9KJ&marketplace=FLIPKART&q=iPhone+SE+2&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=7404e0c5-99f1-495c-9b7b-12c4a1123887.MOBFRFXHYMPBSB5H.SEARCH&ppt=sp&ppn=sp&ssid=ouluq8cx9s0000001723996972992&qH=fc6a8d557b3e3480', 'apple iphone se red 64 gb includes earpods power adapter'],
        'iPhone 12': ['https://www.flipkart.com/apple-iphone-12-blue-64-gb/p/itm5778ad0d0d255?pid=MOBFWBYZ8DNJNY7N&lid=LSTMOBFWBYZ8DNJNY7NMWAWOJ&marketplace=FLIPKART&q=iPhone+12&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=130042cf-3a91-471f-b5ed-2763c516b3db.MOBFWBYZ8DNJNY7N.SEARCH&ppt=sp&ppn=sp&ssid=w8ec0loba80000001723997074119&qH=4bc1881706ce03c1', 'apple iphone 12 blue 64 gb'],
        'iPhone 13': ['https://www.flipkart.com/apple-iphone-13-midnight-128-gb/p/itmca361aab1c5b0?pid=MOBG6VF5Q82T3XRS&lid=LSTMOBG6VF5Q82T3XRSOXJLM9&marketplace=FLIPKART&q=iPhone+13&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=d5459d2e-6510-4732-b1a6-a6cae4dfa9c4.MOBG6VF5Q82T3XRS.SEARCH&ppt=sp&ppn=sp&ssid=wkywbjafsg0000001723997206424&qH=c3d519be0191fbf8', 'apple iphone 13 midnight 128 gb'],
        'iPhone SE 3': ['https://www.flipkart.com/apple-iphone-se-3rd-gen-midnight-128-gb/p/itm2a77125e4e5bc?pid=MOBGC9K3PXUFPSJG&lid=LSTMOBGC9K3PXUFPSJGLJUARV&marketplace=FLIPKART&q=iPhone+SE+3&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=4fc6419a-1bf5-4744-bcc9-904264982723.MOBGC9K3PXUFPSJG.SEARCH&ppt=sp&ppn=sp&ssid=bwrk6tphxc0000001723997268739&qH=91037d0c011c78d1', 'apple iphone se 3rd gen midnight 128 gb'],
        'iPhone 14': ['https://www.flipkart.com/apple-iphone-14-blue-128-gb/p/itmdb77f40da6b6d?pid=MOBGHWFHSV7GUFWA&lid=LSTMOBGHWFHSV7GUFWAFEQJQ4&marketplace=FLIPKART&q=iPhone+14&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=5e4578f4-932c-4279-9dfd-f41adc5b0fa8.MOBGHWFHSV7GUFWA.SEARCH&ppt=sp&ppn=sp&ssid=ipib8wrqgg0000001723997335965&qH=d36118758fc7c034', 'apple iphone 14 blue 128 gb'],
        'iPhone 15': ['https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4?pid=MOBGTAGPTB3VS24W&lid=LSTMOBGTAGPTB3VS24WVZNSC6&marketplace=FLIPKART&q=iPhone+15&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=f315a402-b212-4268-9e97-066c9c2420d9.MOBGTAGPTB3VS24W.SEARCH&ppt=sp&ppn=sp&ssid=9avtlnjz8g0000001723997419016&qH=ea61cd3ec4cf3451', 'apple iphone 15 black 128 gb'],
    },

    'Samsung': {
        'Samsung Galaxy C55': ['https://www.flipkart.com/samsung-galaxy-s23-5g-cream-128-gb/p/itmc77ff94cdf044?pid=MOBGMFFX5XYE8MZN&lid=LSTMOBGMFFX5XYE8MZNRGKCA5&marketplace=FLIPKART&q=Samsung+Galaxy+C55&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=2275caa4-0f96-4d16-b01e-b4afd33e0d3f.MOBGMFFX5XYE8MZN.SEARCH&ppt=sp&ppn=sp&ssid=fzi3bthgts0000001723997982164&qH=708bc4cf919fbcd5', 'samsung galaxy s23 5g cream 128 gb 8 gb ram'],
        'Samsung Galaxy A35': ['https://www.flipkart.com/samsung-galaxy-f15-5g-groovy-violet-128-gb/p/itm3e7d6c7112d45?pid=MOBGYBAVW8HTJH4X&lid=LSTMOBGYBAVW8HTJH4X9VTKYN&marketplace=FLIPKART&q=Samsung+Galaxy+F15&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=4b724f32-c2dd-4d11-832f-e096743d224e.MOBGYBAVW8HTJH4X.SEARCH&ppt=sp&ppn=sp&ssid=pqe179rp1s0000001723998322598&qH=b517d4243329db4d', 'samsung galaxy f15 5g groovy violet 128 gb 6 gb ram'],
        'Samsung Galaxy S23': ['https://www.flipkart.com/samsung-galaxy-s23-5g-cream-128-gb/p/itmc77ff94cdf044?pid=MOBGMFFX5XYE8MZN&lid=LSTMOBGMFFX5XYE8MZNRGKCA5&marketplace=FLIPKART&q=Samsung+Galaxy+S23&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=22c53c7e-ae8a-47f5-93a2-7cd8e5b35374.MOBGMFFX5XYE8MZN.SEARCH&ppt=sp&ppn=sp&ssid=gh6bzuwwwg0000001723998489860&qH=1fe033b290fff2a3', 'samsung galaxy s23 5g cream 128 gb ram'],
        'Samsung Galaxy F54': ['https://www.flipkart.com/samsung-galaxy-f54-5g-stardust-silver-256-gb/p/itme2f1ad33150df?pid=MOBGPN55PEBUKZX2&lid=LSTMOBGPN55PEBUKZX2OBGV0W&marketplace=FLIPKART&q=Samsung+Galaxy+F54&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=b4674157-7d6b-460f-8369-b75c2a8552e3.MOBGPN55PEBUKZX2.SEARCH&ppt=sp&ppn=sp&ssid=9tk5qduxnk0000001723999074315&qH=f991b3b202417155', 'samsung galaxy f54 5g stardust silver 256 gb 8 gb ram'],
        'Samsung Galaxy F14': ['https://www.flipkart.com/samsung-galaxy-f14-5g-omg-black-128-gb/p/itmae94033406fb2?pid=MOBGNBFNE6KGXCCR&lid=LSTMOBGNBFNE6KGXCCRXLTXS7&marketplace=FLIPKART&q=Samsung+Galaxy+F14&store=tyy%2F4io&srno=s_1_6&otracker=search&otracker1=search&fm=Search&iid=46905692-b54e-4826-a1d3-a000edfadfba.MOBGNBFNE6KGXCCR.SEARCH&ppt=sp&ppn=sp&ssid=0wabx0jjq80000001723999147273&qH=6367519029f887af', 'samsung galaxy f14 5g omg black 128 gb 6 gb ram'],
    },

    'Xiomi': {
        'Xiaomi Poco M6 4G': ['https://www.flipkart.com/poco-m6-pro-5g-power-black-128-gb/p/itm5b122ff13027f?pid=MOBGRNZ3FX5XNR2T&lid=LSTMOBGRNZ3FX5XNR2TILGJYM&marketplace=FLIPKART&q=Xiaomi+Poco+M6+4G&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=db2313e9-8b7f-4615-8094-bfeff5b51cfa.MOBGRNZ3FX5XNR2T.SEARCH&ppt=sp&ppn=sp&ssid=dywbt12nr40000001724035230451&qH=9eb798900ec01121', 'poco m6 pro 5g power black 128 gb 4 gb ram'],
        'REDMI Note 12': ['https://www.flipkart.com/redmi-note-12-lunar-black-64-gb/p/itm6756d6e7a86be?pid=MOBGNYHZJGGE3ZHM&lid=LSTMOBGNYHZJGGE3ZHMCSWYEM&marketplace=FLIPKART&q=Xiaomi+Redmi+13&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=a1a0879d-22ce-453b-83cc-2bc161bd1e14.MOBGNYHZJGGE3ZHM.SEARCH&ppt=sp&ppn=sp&ssid=lllzqyj7k00000001724035352817&qH=517aa81e18175a69', 'redmi note 12 lunar black 64 gb 6 gb ram'],
        'Xiaomi Poco F6 Pro': ['https://www.flipkart.com/poco-m6-pro-5g-power-black-128-gb/p/itm5b122ff13027f?pid=MOBGRNZ3FX5XNR2T&lid=LSTMOBGRNZ3FX5XNR2TILGJYM&marketplace=FLIPKART&q=Xiaomi+Poco+F6+Pro&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=7c23e521-0927-418c-a4e4-05c198e538b4.MOBGRNZ3FX5XNR2T.SEARCH&ppt=sp&ppn=sp&ssid=xbukul75r40000001724035518034&qH=510e6b8d0d7f8f8d', 'poco m6 pro 5g power black 128 gb 6 gb ram'],
        'Redmi Note 8': ['https://www.flipkart.com/redmi-note-8-moonlight-white-64-gb/p/itmd9fd42df891ce?pid=MOBFHGTKYGZBXNGK&lid=LSTMOBFHGTKYGZBXNGKGULMAX&marketplace=FLIPKART&q=Xiaomi+Redmi+Note+13R&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=c54ef7df-aff5-47a6-992a-576ea24b20e1.MOBFHGTKYGZBXNGK.SEARCH&ppt=sp&ppn=sp&ssid=wpw2km2uio0000001724035636790&qH=e7e8ecd92889cf2c', 'redmi note 8 moonlight white 64 gb'],
        'REDMI Note 10T 5G': ['https://www.flipkart.com/redmi-note-10t-5g-metallic-blue-64-gb/p/itm7a558068a9f23?pid=MOBGC7QFTGDSWQZN&lid=LSTMOBGC7QFTGDSWQZNQOXYJA&marketplace=FLIPKART&q=Xiaomi+Redmi+Turbo+3&store=tyy%2F4io&srno=s_1_5&otracker=search&otracker1=search&fm=Search&iid=17532536-651d-43ee-8273-acfeea530b95.MOBGC7QFTGDSWQZN.SEARCH&ppt=sp&ppn=sp&ssid=jzhl0cy4e80000001724035736682&qH=95af39a13fceab95', 'redmi note 10t 5g metallic blue 64 gb'],
        'Redmi 8': ['https://www.flipkart.com/redmi-8-emerald-green-64-gb/p/itme0903bcb8a2cb?pid=MOBFKPYDTSZ8SFHH&lid=LSTMOBFKPYDTSZ8SFHHXLSP3R&marketplace=FLIPKART&q=Xiaomi+Redmi+13R&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=7dca8bf1-7dca-4f75-99cd-866a556b1521.MOBFKPYDTSZ8SFHH.SEARCH&ppt=sp&ppn=sp&ssid=b16m23jvyo0000001724036002293&qH=567874839ff95a90', 'redmi 8 emerald green 64 gb'],
        'POCO F1': ['https://www.flipkart.com/poco-f1-steel-blue-128-gb/p/itm55025e3c0935a?pid=MOBGQZ55AYWGEYEU&lid=LSTMOBGQZ55AYWGEYEUL2HUVW&marketplace=FLIPKART&q=poco+f1&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=search-autosuggest&iid=85dffdd6-b376-4481-b187-7d070381995c.MOBGQZ55AYWGEYEU.SEARCH&ppt=sp&ppn=sp&ssid=kvy5vfvquo0000001724036934787&qH=f6f38324df02133a', ''],
        'POCO X5 Pro 5G': ['https://www.flipkart.com/poco-x5-pro-5g-horizon-blue-256-gb/p/itm7d7b6b78895bc?pid=MOBGMDKQ2NHTBHJM&lid=LSTMOBGMDKQ2NHTBHJMQ7AMXN&marketplace=FLIPKART&q=poco+phones&store=tyy%2F4io&srno=s_1_14&otracker=search&otracker1=search&fm=Search&iid=5773efba-7366-4029-a1d0-c30331f2b657.MOBGMDKQ2NHTBHJM.SEARCH&ppt=sp&ppn=sp&ssid=ggl6l53t680000001724037034372&qH=2aad366020d6d072', ''],
        'POCO F5 5G': ['https://www.flipkart.com/poco-f5-5g-carbon-black-256-gb/p/itma0ee4e5847868?pid=MOBGP2G52Z3RS2ZE&lid=LSTMOBGP2G52Z3RS2ZEY8WNZX&marketplace=FLIPKART&q=poco+phones&store=tyy%2F4io&srno=s_1_12&otracker=search&otracker1=search&fm=Search&iid=5773efba-7366-4029-a1d0-c30331f2b657.MOBGP2G52Z3RS2ZE.SEARCH&ppt=sp&ppn=sp&ssid=ggl6l53t680000001724037034372&qH=2aad366020d6d072', ''],
        'POCO X3 Pro': ['https://www.flipkart.com/poco-x3-pro-graphite-black-128-gb/p/itm736059fa07afb?pid=MOBGFKNFRJDN3DS4&lid=LSTMOBGFKNFRJDN3DS43QXYLC&marketplace=FLIPKART&q=poco+phones&store=tyy%2F4io&srno=s_2_26&otracker=search&otracker1=search&fm=Search&iid=db723c6c-0c47-464e-bb30-5087a0bb48a3.MOBGFKNFRJDN3DS4.SEARCH&ppt=sp&ppn=sp&qH=2aad366020d6d072', ''],
        'POCO X3': ['https://www.flipkart.com/poco-x3-cobalt-blue-128-gb/p/itm5eabfda5f2dd4?pid=MOBFVQJ5TZTF5JHC&lid=LSTMOBFVQJ5TZTF5JHCO0EDJU&marketplace=FLIPKART&q=poco+phones&store=tyy%2F4io&srno=s_2_33&otracker=search&otracker1=search&fm=Search&iid=db723c6c-0c47-464e-bb30-5087a0bb48a3.MOBFVQJ5TZTF5JHC.SEARCH&ppt=sp&ppn=sp&qH=2aad366020d6d072', ''],
        'POCO X2': ['https://www.flipkart.com/poco-x2-phoenix-red-256-gb/p/itm065a12f7b9503?pid=MOBFZGJ6BYAPAHBH&lid=LSTMOBFZGJ6BYAPAHBH9YCFJU&marketplace=FLIPKART&q=poco+phones&store=tyy%2F4io&srno=s_2_34&otracker=search&otracker1=search&fm=Search&iid=db723c6c-0c47-464e-bb30-5087a0bb48a3.MOBFZGJ6BYAPAHBH.SEARCH&ppt=sp&ppn=sp&qH=2aad366020d6d072', ''],
        'POCO M2 Pro': ['https://www.flipkart.com/poco-m2-pro-two-shades-black-128-gb/p/itm4ce7da562a7bb?pid=MOBFT7MKJXZPFPMS&lid=LSTMOBFT7MKJXZPFPMSK00QGH&marketplace=FLIPKART&q=poco+phones&store=tyy%2F4io&srno=s_2_39&otracker=search&otracker1=search&fm=Search&iid=db723c6c-0c47-464e-bb30-5087a0bb48a3.MOBFT7MKJXZPFPMS.SEARCH&ppt=sp&ppn=sp&qH=2aad36,6020d6d072', ''],
        'POCO X4 Pro 5G': ['https://www.flipkart.com/poco-x4-pro-5g-laser-blue-128-gb/p/itmeb324bd268ef4?pid=MOBGCGZZDHZ2HJU8&lid=LSTMOBGCGZZDHZ2HJU8ONUSOK&marketplace=FLIPKART&q=poco+phones&store=tyy%2F4io&srno=s_2_40&otracker=search&otracker1=search&fm=Search&iid=db723c6c-0c47-464e-bb30-5087a0bb48a3.MOBGCGZZDHZ2HJU8.SEARCH&ppt=sp&ppn=sp&qH=2aad366020d6d072', ''],
    },

    'Oneplus': {
        'OnePlus Nord CE 2 Lite 5G': ['https://www.flipkart.com/oneplus-nord-ce-2-lite-5g-blue-tide-128-gb/p/itm7acae55b999e6?pid=MOBGMFREBAHZQGY9&lid=LSTMOBGMFREBAHZQGY9TPTG8U&marketplace=FLIPKART&q=oneplus+nord&store=tyy%2F4io&srno=s_1_11&otracker=search&otracker1=search&fm=search-autosuggest&iid=467f8b55-3d59-449d-baaa-9658706a0b94.MOBGMFREBAHZQGY9.SEARCH&ppt=sp&ppn=sp&ssid=mmzhkixavk0000001724036441595&qH=e8b736bf4fa84421', ''],
        'OnePlus Nord CE 3 Lite 5G': ['https://www.flipkart.com/oneplus-nord-ce-3-lite-5g-pastel-lime-128-gb/p/itm2cd5a4e659035?pid=MOBGZJ3WM5SGTGVZ&lid=LSTMOBGZJ3WM5SGTGVZSKDCXZ&marketplace=FLIPKART&q=oneplus+nord&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=search-autosuggest&iid=467f8b55-3d59-449d-baaa-9658706a0b94.MOBGZJ3WM5SGTGVZ.SEARCH&ppt=sp&ppn=sp&ssid=mmzhkixavk0000001724036441595&qH=e8b736bf4fa84421', ''],
    }
}
# phone_list.py


from flask import jsonify


def send_popup_message(status, status_message):
    send_dict = {'status': status, 'message': status_message}
    print(f'sending message: {status_message}')
    return jsonify(send_dict)
