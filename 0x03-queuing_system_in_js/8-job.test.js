import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', function () {
  this.timeout(5000); // Increase timeout to 5000ms
  let queue;

  before(() => {
    queue = kue.createQueue();
  });

  afterEach(done => {
    // Clear all jobs from the queue after each test
    kue.Job.rangeByType('push_notification_code_3', 'active', 0, -1, 'asc', (err, selectedJobs) => {
      if (err) return done(err);
      selectedJobs.forEach(job => job.remove());
      done();
    });
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(null, queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', done => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Check after a delay
    setTimeout(() => {
      kue.Job.rangeByType('push_notification_code_3', 'inactive', 0, -1, 'asc', (err, inactiveJobs) => {
        if (err) return done(err);

        expect(inactiveJobs.length).to.equal(2);
        expect(inactiveJobs[0].type).to.equal('push_notification_code_3');
        expect(inactiveJobs[0].data).to.deep.equal(jobs[0]);
        expect(inactiveJobs[1].type).to.equal('push_notification_code_3');
        expect(inactiveJobs[1].data).to.deep.equal(jobs[1]);
        done();
      });
    }, 3000); // Increased delay
  });
});

