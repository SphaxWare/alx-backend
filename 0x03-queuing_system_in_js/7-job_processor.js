import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100); // Track the progress of the job of 0 out of 100

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100); // Track the progress to 50%

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done(); // Call the done callback
}

// Create a queue with Kue
const queue = kue.createQueue();

// Process jobs in the queue 'push_notification_code_2' with concurrency of 2 jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
