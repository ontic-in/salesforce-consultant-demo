// F1: Create Case with Product Line
// F2: Customer Tier formula populates from Account
// F3: Waiting on Customer status works
// F4: Resolved status closes case

Account acct = [SELECT Id, Name, Customer_Tier__c FROM Account WHERE Id = '001dN00000oz1NNQAY'];
System.debug('F2-SETUP: Account=' + acct.Name + ', Tier=' + acct.Customer_Tier__c);

// F1: Create Case with Product Line
Case testCase = new Case(
    Subject = 'US-003 QA Test Case',
    Status = 'New',
    Priority = 'High',
    Product_Line__c = 'Core Platform',
    AccountId = acct.Id,
    Origin = 'Phone',
    Type = 'Technical Issue / Bug Report'
);
insert testCase;
System.debug('F1-PASS: Case created with Id=' + testCase.Id + ', Product_Line__c=' + testCase.Product_Line__c);

// F2: Verify Customer Tier formula
Case verifyCase = [SELECT Id, Customer_Tier__c, Product_Line__c FROM Case WHERE Id = :testCase.Id];
System.debug('F2-RESULT: Customer_Tier__c=' + verifyCase.Customer_Tier__c);
if (verifyCase.Customer_Tier__c == 'Gold') {
    System.debug('F2-PASS: Formula correctly shows Gold from Account');
} else {
    System.debug('F2-FAIL: Expected Gold, got ' + verifyCase.Customer_Tier__c);
}

// F3: Update to Waiting on Customer
testCase.Status = 'Waiting on Customer';
update testCase;
Case wocCase = [SELECT Id, Status, IsClosed FROM Case WHERE Id = :testCase.Id];
if (wocCase.Status == 'Waiting on Customer' && !wocCase.IsClosed) {
    System.debug('F3-PASS: Status=Waiting on Customer, IsClosed=false');
} else {
    System.debug('F3-FAIL: Status=' + wocCase.Status + ', IsClosed=' + wocCase.IsClosed);
}

// F4: Update to Resolved (should close case)
testCase.Status = 'Resolved';
update testCase;
Case resolvedCase = [SELECT Id, Status, IsClosed FROM Case WHERE Id = :testCase.Id];
if (resolvedCase.Status == 'Resolved' && resolvedCase.IsClosed) {
    System.debug('F4-PASS: Status=Resolved, IsClosed=true');
} else {
    System.debug('F4-FAIL: Status=' + resolvedCase.Status + ', IsClosed=' + resolvedCase.IsClosed);
}

// Cleanup: Delete test case
delete testCase;
System.debug('CLEANUP: Test case deleted');
