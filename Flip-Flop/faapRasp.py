import ibmiotf.application
import ibmiotf.gateway
from ibmiotf.codecs import jsonCodec, jsonIotfCodec

def myAppEventCallback(event):
	print("Received live data from %s (%s) sent at %s: hello=%s x=%s" % (event.deviceId, event.deviceType, event.timestamp.strftime("%H:%M:%S"), data['hello'], data['x']))

def myOnPublishCallback():
	print("Confirmed event %s received by IBM Watson IoT Platform\n" % x)


def sendDataBluemix(rfidCode):
	organization = "aaeigm"

	gatewayType = "TirantA"
	gatewayId = "gtw"

	authMethod = "token"
	authToken = "password"

	'''Here starts the code to send data to Watson IoT platform'''
	# Initialize the device client.
	try:
		gatewayOptions = {"org": organization, "type": gatewayType, "id": gatewayId, "auth-method": authMethod, "auth-token": authToken}
		gatewayCli = ibmiotf.gateway.Client(gatewayOptions)

	except Exception as e:
		print("Caught exception connecting device: %s" % str(e))


	gatewayCli.connect()

	myGatewayData = {'status':'alessandro'}
	myDataSensor = {'dataSen': 'teste'}

	gatewayCli.setMessageEncoderModule('json', jsonCodec)

	gatewayCli.setMessageEncoderModule('json', jsonCodec)
	try:
		gatewaySuccess = gatewayCli.publishGatewayEvent("greeting", "json", myGatewayData, qos=1,
													on_publish=myOnPublishCallback)
		deviceSuccess = gatewayCli.publishDeviceEvent("raspProd", rfidCode, "data", "json", myDataSensor, qos=1,
												  on_publish=myOnPublishCallback)
	except Exception as e:
		print("Caught exception publishing device: %s" % str(e))

	if not gatewaySuccess:
		print("Gateway not connected to IBM Watson IoT Platform while publishing from Gateway")

	if not deviceSuccess:
		print("Gateway not connected to IBM Watson IoT Platform while publishing from Gateway on behalf of a device")

	gatewayCli.disconnect()


if __name__ == "__main__":
	sendDataBluemix("rfid2");
	sendDataBluemix("rfid1");
