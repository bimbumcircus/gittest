#! python
import os

def valami2(this):
    pass

def valami(this):
    pass

def getAlarmTypes(fineName):
        

    eventTypes = {
            'other':1,
            'communicationsAlarm': 2,
            'qualityOfServiceAlarm': 3,
            'processingErrorAlarm': 4,
            'equipmentAlarm': 5,
            'environmentalAlarm': 6,
            'integrityViolation': 7,
            'operationalViolation': 8,
            'physicalViolation': 9,
            'securityServiceOrMechanismViolation': 10,
            'timeDomainViolation': 11
            } 

    alarms = {'version':'v1'}
    data = []

    with open('EPG_FmAlarmModel.txt', 'r') as f:
        data = f.readlines()


    state = 'none'
    fm_alarm_model = ''
    fm_alarm_type = ''
    fm_alarm = {}
    alarm_list = []
    alarm_dict = {}


    
    for line in data:
        if line.find('FmAlarmModel=') != -1:
            fm_alarm_model =  (line.split('=')[1]).strip()

        if line.find('FmAlarmType=') != -1:
            if 'fm_alarm_type' in fm_alarm.keys():
                alarm_list.append(fm_alarm)
                alarm_dict[fm_alarm['fm_alarm_type']] = fm_alarm
            
            fm_alarm = {}    
            fm_alarm_type = (line.split('=')[1]).strip()

            fm_alarm = {'fm_alarm_type': fm_alarm_type}
            fm_alarm['FmAlarmModel'] = fm_alarm_model
                    
        if line.find('additionalText=') != -1:
            fm_alarm['additionalText'] = (line.split('=')[1]).strip()

        if line.find('eventType=') != -1:
            fm_alarm['eventType'] = (line.split('=')[1]).strip()

        if line.find('majorType=') != -1:
            fm_alarm['majorType'] = int((line.split('=')[1]).split()[0])

        if line.find('minorType=') != -1:
            fm_alarm['minorType'] = int((line.split('=')[1]).split()[0])

        if line.find('moClasses=') != -1:
            fm_alarm['moClasses'] = (line.split('=')[1]).strip()

        if line.find('probableCause=') != -1:
            fm_alarm['probableCause'] = ((line.split('=')[1]).split()[0])

        if line.find('specificProblem=') != -1:
            fm_alarm['specificProblem'] = (line.split('=')[1]).strip()


    for alarm in alarm_list:
        eventTypefound = False;
        for key in eventTypes.keys():
            if eventTypefound == False and alarm['eventType'].find(key.upper()) != -1:
                alarm['eventType'] = eventTypes[key]
                eventTypefound = True

        

    for alarm in alarm_dict.keys():
        print(alarm + '=>' + str(alarm_dict[alarm]))



    #  FmAlarmModel=9
    # 2017-08-31 12:57:43$      fmAlarmModelId="9"
    # 2017-08-31 12:57:43$      FmAlarmType=KeyFileFault
    # 2017-08-31 12:57:43$         additionalText="Key file fault in Managed Element" <read-only>
    # 2017-08-31 12:57:43$         configuredSeverity=[] <empty>
    # 2017-08-31 12:57:43$         defaultSeverity=[] <empty> <read-only>
    # 2017-08-31 12:57:43$         eventType=QUALITYOFSERVICEALARM <read-only>
    # 2017-08-31 12:57:43$         fmAlarmTypeId="KeyFileFault"
    # 2017-08-31 12:57:43$         isStateful=true <read-only>
    # 2017-08-31 12:57:43$         majorType=193 <read-only>
    # 2017-08-31 12:57:43$         minorType=393221 <read-only>
    # 2017-08-31 12:57:43$         moClasses="Lm" <read-only> <deprecated>
    # 2017-08-31 12:57:43$         probableCause=159 <read-only>
    # 2017-08-31 12:57:43$         specificProblem="License Management, Key File Fault" <read-only>
    # 2017-08-31 12:57:43$      FmAlarmType=LicenseKeyNotAvailable
    # 2017-08-31 12:57:43$         additionalText="Key missing for feature or capacity" <read-only>
    # 2017-08-31 12:57:43$         configuredSeverity=[] <empty>
    # 2017-08-31 12:57:43$         defaultSeverity=[] <empty> <read-only>
    # 2017-08-31 12:57:43$         eventType=QUALITYOFSERVICEALARM <read-only>
    # 2017-08-31 12:57:43$         fmAlarmTypeId="LicenseKeyNotAvailable"
    # 2017-08-31 12:57:43$         isStateful=true <read-only>
    # 2017-08-31 12:57:43$         majorType=193 <read-only>
    # 2017-08-31 12:57:43$         minorType=393217 <read-only>
    # 2017-08-31 12:57:43$         moClasses="Lm" <read-only> <deprecated>
    # 2017-08-31 12:57:43$         probableCause=159 <read-only>
    # 2017-08-31 12:57:43$         specificProblem="License Management, License Key Not Available" <read-only>
    return alarm_list



def sendAlarm(name, parameter):
    pass
