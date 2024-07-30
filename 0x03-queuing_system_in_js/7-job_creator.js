import kue from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

// Create a queue
const queue = kue.createQueue();

// for each job loop
jobs.forEach((jobData, index) => {
  // Create a new job to the queue push_notification_code_2
  const job = queue.create('push_notification_code_2', jobData)
    .save((err) => {
      // If there is no error, log to the console Notification...
      if (!err) {
        console.log('Notification job created: ${job.id}');
      }
    });

  // On the job completion, log to the console Notification job JOB_ID completed
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  // On the job failure, log to the console Notification job JOB_ID failed: ERROR
  }).on('failed', (err) => {
    console.log(`Notification job ${job.id} failed: ${err}`);
  // On the job progress, log to the console Notification job JOB_ID PERCENTAGE% complete
  }).on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
});
