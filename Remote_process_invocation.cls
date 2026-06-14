public with sharing class Remote_Process_Invocation {
    String recordName = '';
    String body = ''; 

    public Remote_Process_Invocation(String URLpath, String recordNameInput) {
        this.recordName = recordNameInput;
        this.body = '{"message_id": ' + String.valueof(System.currentTimeMillis()) + ', "account_id": "' + this.recordName + '"}';
        Remote_CALLOUT(URLpath);   
    }

    void Remote_CALLOUT(String URLpath) {
        HttpRequest req = new HttpRequest();
        req.setEndpoint('callout:Python_endpoint_named_credential' + URLpath);
        req.setMethod('POST');
        req.setHeader('Content-Type', 'application/json');
        req.setBody(this.body);
        Http http = new Http();
        HttpResponse res = http.send(req);

        System.debug('Status Code: ' + res.getStatusCode());
        System.debug('Response Body: ' + res.getBody());
    }
}