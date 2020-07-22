import login
import queueing_patient 

patient_q = queueing_patient.Queue()
patient_q_priority = queueing_patient.Queue()

def varify_email(email):
    '''
    str --> bool
    '''
    
    for char in email:
        if char == '@':
            return email[-4:] == '.com'

    return False


def queueing(patient):

    # true stands for the emergency
    if patient.priority:
        patient_q_priority.add(patient)
    else:
        patient_q.add(patient)

def dequeueing():
    if patient_q_priority.isEmptyQueue() and not (patient_q.isEmptyQueue()):
        return patient_q.retrive()
    elif not (patient_q_priority.isEmptyQueue()):
        return patient_q_priority.retrive()

 
    

if __name__ == '__main__':
    p1 = login.Patient("tom", "2000-12-03", "normal")
    p2 = login.Patient("jerry", "2000-12-03", "normal")
    p3 = login.Patient("yichen", "2000-12-03", "priority")
    p4 = login.Patient("himel", "2000-12-03", "priority")
    p3.emergency()
    p4.emergency()
    queueing(p1)
    queueing(p2)
    queueing(p3)
    queueing(p4)
    #patient_q.priorized(p3)
    #patient_q.priorized(p4)
    print("############")
    #print(p3)
    #print(patient_q)
    #print(str(patient_q.retrive()))
    print(dequeueing())
    print(dequeueing())
    print(dequeueing())
    print(dequeueing())
