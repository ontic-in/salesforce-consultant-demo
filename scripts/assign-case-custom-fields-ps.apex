// Assign Case_Custom_Fields permission set to all Relay Logic users + admins
PermissionSet ps = [SELECT Id FROM PermissionSet WHERE Name = 'Case_Custom_Fields' LIMIT 1];

List<User> users = [
    SELECT Id, Name FROM User
    WHERE IsActive = true
    AND UserType = 'Standard'
    AND Id NOT IN (SELECT AssigneeId FROM PermissionSetAssignment WHERE PermissionSetId = :ps.Id)
];

List<PermissionSetAssignment> assignments = new List<PermissionSetAssignment>();
for (User u : users) {
    assignments.add(new PermissionSetAssignment(AssigneeId = u.Id, PermissionSetId = ps.Id));
    System.debug('Assigning to: ' + u.Name);
}

if (!assignments.isEmpty()) {
    insert assignments;
    System.debug('Assigned Case_Custom_Fields to ' + assignments.size() + ' users');
} else {
    System.debug('All standard users already have Case_Custom_Fields');
}
