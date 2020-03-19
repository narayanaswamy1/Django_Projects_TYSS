from django.db import models

class Employee(models.Model):
    employeeId = models.CharField()
    employeeName = models.CharField()
    empFathersName = models.CharField()
    empMothersName = models.CharField()
    empBloodGroup = models.CharField()
    empDateofBirth = models.CharField()
    empGender = models.CharField()
    empMaritalStatus = models.CharField()
    empSpouseName = models.CharField()
    empDesignation = models.CharField()
    empEmergencyContact = models.CharField()
    empPermanentAddress = models.CharField()
    empPresentAddress = models.CharField()

    empPostGraduation = models.CharField()
    empPGUniversity = models.CharField()
    empPGYop = models.CharField()
    
    empUnderGraduation = models.CharField()
    empUGUniversity = models.CharField()
    empUGYop = models.CharField()
    
    emp12th = models.CharField()
    emp12thBoard = models.CharField()
    emp12thYop = models.CharField()
    
    emp10th = models.CharField()
    emp10thBoard = models.CharField()
    emp10thYop = models.CharField()

    
    employer1 = models.CharField()
    e1designation = models.CharField()
    e1from = models.CharField()
    e1to = models.CharField()

    employer2 = models.CharField()
    e2designation = models.CharField()
    e2from = models.CharField()
    e1to = models.CharField()

    dateofJoining = models.CharField()
    panNo = models.CharField()
    uanNo = models.CharField()
    aadhaarNo = models.CharField()
    bankAccNo = models.CharField()
    bankIFSC = models.CharField()
    employeeSign = models.CharField()
    esigndate = models.CharField()