#!/usr/bin/env python
# coding=utf-8
from create_instance_sqlalchemy import *
from sqlalchemy import ForeignKey                                                       
from sqlalchemy.orm import relationship                                                 
from sqlalchemy.ext.declarative import declarative_base

class Address(Base):                                                                    
    __tablename__ = 'addresses'                                                         
    id = Column(Integer, primary_key=True)                                              
    email_address = Column(String(50), nullable=False)                                  
    user_id = Column(Integer, ForeignKey('users.id'))                                   
    user = relationship("User", back_populates='addresses')                             
                                                                                        
    def __repr__(self):                                                                 
        return f"<Address(email_address={self.email_address})>"                         
                                                                                        
Base.metadata.create_all(engine)                                                        
