import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine , select , update
from datetime import datetime
from sqlalchemy.ext.automap import automap_base
from faker import Faker
from faker.providers import BaseProvider
from collections import OrderedDict



# Connect to the database

class MyProvider(BaseProvider):
    __provider__ = 'fake_product' 
    
    
    product =  OrderedDict({"Electronics" : ["Smartphone","Laptop","Tablet","Smart TV","Gaming Console"],
                            "Clothing" : ['T-shirts', 'Jeans', 'Sneakers', 'Dresses', 'Jackets'],
                            "Books" : ['Hardcover Books', 'Paperback Books', 'E-books', 'Audiobooks', 'Comic Books'],
                            "Home & Garden" : ['Furniture', 'Appliances', 'Home Decor', 'Gardening Tools', 'Bedding and Linens'],
                            "Beauty" : ['Skincare', 'Makeup', 'Fragrances', 'Hair Care', 'Personal Care'],
                            "Toys" : ['Action Figures', 'Dolls', 'Board Games', 'LEGO Sets', 'Remote Control Cars'],
                            "Sports & Outdoors" : ['Camping Gear', 'Fitness Equipment', 'Bicycles', 'Fishing Gear', 'Outdoor Clothing'],
                            "Food & Beverages" : ['Coffee', 'Tea', 'Wine', 'Chocolate', 'Snacks'],
                            "Health" : ['Vitamins', 'Supplements', 'Protein Powder', 'First Aid Kits', 'Fitness Trackers'],
                            "Automotive" :['Tires', 'Car Batteries', 'Motor Oil', 'Car Accessories', 'GPS Navigation']

    
    })
    
    def fake_product(self):
        key = self.random_element(self.product.keys())
        value = random.choice(self.product[key])
        return key,value 



def insert_category(Category):
    data = {"Electronics" : "The best deals on the latest electronics!",
                   "Clothing" : "Trendy clothing for every occasion", 
                  "Books" :"Discover the best books for all ages and interests.",
                  "Home & Garden" : "Upgrade your home and garden with our stylish products.", 
                  "Beauty" : "Get the latest beauty products for flawless skin.", 
                  "Toys" : "Fun toys for kids of all ages!", 
                  "Sports & Outdoors" : "Sports and outdoor gear for every adventure.",
                  "Food & Beverages" : "Delicious food and beverages for any occasion." ,
                  "Health" : "Stay healthy and fit with our wellness products.", 
                  "Automotive" : "Upgrade your ride with our automotive accessories."}
    





    #count = session.query(Category).count()
    #print(count)
    for i in data:
        creation_date = fake.date_time_between(start_date , end_date )
        update_date = fake.date_time_between(creation_date , end_date )
        stmt = select(Category).where(Category.category_name == i )
        result = conn.execute(stmt).fetchone() 
        if result == None:
            C = Category(category_name = i , category_description = data[i], creation_date = creation_date , update_date = update_date )
            session.add(C)
        session.commit()


    
def add_new_product(n,Product,Category):
    for i in range(n):
        creation_date = fake.date_time_between(start_date , end_date )
        update_date = fake.date_time_between(creation_date , end_date )
        id = fake.random_int(min=1,max=100)
        price = round( random.uniform(50,1000) , 2 ) 
        quantity = fake.random_int(min=1,max=1000)
        p = fake.fake_product()
        
        product_category = p[0]
        
        product_namee = p[1]
        stmt = select(Category.id).select_from(Category).where( Category.category_name == product_category)
        result = conn.execute(stmt).fetchone() 

        stmt2 = select(Product.id,Product.stock_quantity).select_from(Product).where( Product.product_name == product_namee)
        result2 = conn.execute(stmt2).fetchone() 

        if result2 != None :
            stmt3 = (update(Product).where(Product.id == result2[0]).values(stock_quantity =  result2[1]+1 ))  
            conn.execute(stmt3)
            print(f"update:{result2[0]} : {result2[1]}",)
            session.commit()
        else:
            C = Product( category_id = result[0], product_name = product_namee , price = price , stock_quantity = quantity , creation_date = creation_date , update_date = update_date )
            session.add(C)
            session.commit()
        

    print(f"add {n} product done")

def add_customer(n,Customer):
    for i in range(n):
        name = fake.name()
        adress = fake.street_address()
        gender = random.choice(['M','F'])
        creation_date = fake.date_time_between(start_date , end_date )
        update_date  = fake.date_time_between(creation_date , end_date )
        C = Customer(customer_name = name ,adresse = adress  , gender = gender , creation_date = creation_date , update_date = update_date)
        session.add(C)
        session.commit()
    print(f"add {n} customer done")


def add_sales(n,Sales,Product,Customer):
    for i in range(n):
        
        r1 = select(Customer.id).select_from(Customer)
        customer_id = random.choice(conn.execute(r1).fetchall()) # result is list of tuples
        r2 = select(Product.id).select_from(Product)
        
        product_id = random.choice(conn.execute(r2).fetchall())  # result is list of tuples
        r3 = conn.execute(select(Product.creation_date).select_from(Product).where(product_id[0] == Product.id )).fetchone()

        creation_date = r3[0]
        #print(conn.execute(r2).fetchall())
        creation_date = fake.date_time_between(creation_date , end_date )
        update_date  = fake.date_time_between(creation_date , end_date )
        r3 = select(Product.price).select_from(Product).where(product_id[0] == Product.id )
        total_price = conn.execute(r3).fetchone()
        
        C = Sales(product_id = product_id[0] ,customer_id = customer_id[0] , total_price = total_price[0], sale_date = creation_date , creation_date = creation_date , update_date = update_date)
        session.add(C)
        session.commit()
    print(f"add {n} sales done")

if __name__ == '__main__':
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 9, 30)


    db_name = 'database'
    db_user = 'softbrain'
    db_pass = 'softbrain'
    db_host = 'db'
    db_port = '5432'


    db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
    engine = create_engine(db_string)
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Category = Base.classes.category
    Product = Base.classes.product
    Customer = Base.classes.customer
    Sales = Base.classes.sales
    print("connection done succefully")
    Session = sessionmaker(bind=engine)
    session = Session()
    print("sesssion done succefully")
    fake = Faker()
    fake.add_provider(MyProvider)
    conn = engine.connect()
    n = 10000
    insert_category(Category)
    add_new_product(n,Product,Category)
    add_customer(n,Customer)
    add_sales(n,Sales,Product,Customer)
            


    