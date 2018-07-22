from pysnmp.entity.rfc3413.oneliner import ntforg
from alarmTypeParser.py import getAlarmTypes
# something added

getAlarmTypes('')
ntfOrg = ntforg.NotificationOriginator()

#errorIndication = ntfOrg.sendNotification(
#    ntforg.CommunityData('public'),
#    ntforg.UdpTransportTarget(('localhost', 162)),
#    'trap',
#    ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmWarning'),
#    (ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveManagedObject' ), 'MO=10,DC=20'),
#    (ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveMajorType' ), 13),
#    (ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveMinorType' ), 1),
#    (ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveLastSequenceNo' ), 21),
#    (ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveEventType' ), 1),
#    (ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveEventTime' ), '2017-09-01'),
#    (ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveProbableCause' ), 1),
#    (ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveSpecificProblem' ), 'valami oriasi gebasz van'),
#    (ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmNObjAdditionalText' ), 'meg nagyobb gebasz lett!'),
#    (ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmNObjMoreAdditionalText' ), 'false'),
#    (ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveProbableCause' ), 1),
#    (ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmNObjResourceId' ), 1)
#)
#

def sendEricssonAlarm(alarm):
	errorIndication = ntfOrg.sendNotification(
		ntforg.CommunityData('public'),
		ntforg.UdpTransportTarget(('localhost', 162)),
		'trap',
		ntforg.MibVariable('ERICSSON-ALARM-MIB', alarm['severity']),
		(ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveManagedObject' ), alarm['moClasses']),
		(ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveMajorType' ), alarm['majorType']),
		(ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveMinorType' ), alarm['minorType']),
		(ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveLastSequenceNo' ), alarm['lastSequenceNumber']),
		(ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveEventType' ), alarm['eventType']),
		(ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveEventTime' ), alarm['eventTime']),
		(ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveProbableCause' ), alarm['probableCause']),
		(ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveSpecificProblem' ),alarm['specificProblem']),
		(ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmNObjAdditionalText' ),alarm['additionalText']),
		(ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmNObjMoreAdditionalText' ), 'false'),
		(ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmActiveProbableCause' ), alarm['probableCause']),
		(ntforg.MibVariable('ERICSSON-ALARM-MIB', 'eriAlarmNObjResourceId' ), alarm['resourceId'])
	)



if errorIndication:
    print('Notification not sent: %s' % errorIndication)

