from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'


POSTGRESQL_DATABASE_URL = 'postgresql://deploy_database_yn0f_user:Tq8rgmt4z7DxVVisqGzI6Euuglz8o50B@dpg-d5j6lqogjchc73cvb3dg-a/deploy_database_yn0f'
# MYSQL_DATABASE_URL = 'mysql+pymysql://root:test1234@127.0.0.1:3306/todoapplicationdatabase'
#  connect_args={'check_same_thread':False} this will allow sqlite to communicate only with one thread

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})
engine = create_engine(POSTGRESQL_DATABASE_URL, connect_args={'check_same_thread':False})

#engine = create_engine(MYSQL_DATABASE_URL)


# To have full control of the database we set autocommit and autoflush to False
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Database object to interact with
Base = declarative_base()