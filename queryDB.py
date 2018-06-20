def getx(ret_category):
    import psycopg2
    try:
        conn = psycopg2.connect("dbname='d8rajubfe1hqd9' user='qahtzkgwxrvssb' host='ec2-54-75-233-92.eu-west-1.compute.amazonaws.com' password='7orJtuGsLXaqgmLb4Rg80eG0ZM'",psycopg2.extensions.register_type(psycopg2.extensions.UNICODE), psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY))
    
    
    except:
        print "I am unable to connect to the database"
        
    try:
        cur = conn.cursor()

    except:
        print "Connection error"
    if len(ret_category)>0:
        cur.execute("SELECT * FROM scrap WHERE category = '%s'" %ret_category)
        rows = cur.fetchall()
        ad_list = []
        for row in rows:
            product_name =row[0]
            price = row[1]
            link = row[2]
            image = row[3]
            category = row[4]
            ad_id = row[5]
            ad_set = {'product_name':product_name, 'price':price, 'link':link, 'image':image, 'category':category, 'ad_id':ad_id}
            ad_list.append(ad_set)
        return ad_list
    else:
        cur.execute("""SELECT * FROM scrap;""")
        rows = cur.fetchall()
        ad_list = []
        for row in rows:
            product_name =row[0]
            price = row[1]
            link = row[2]
            image = row[3]
            category = row[4]
            ad_id = row[5]
            ad_set = {'product_name':product_name, 'price':price, 'link':link, 'image':image, 'category':category, 'ad_id':ad_id}
            ad_list.append(ad_set)
        return ad_list
        
