#include <queue>
#include <mutex>
#include <condition_variable>
#include <string>
#include <iostream>
#include <thread>
using namespace std;

// Message structure
class Message {
    public:
    int messageType;
    string payload;
    // Add any other fields as needed
};

class MessageQueue {

    private:
        queue<Message> queue_;
        mutex mutex_;
        condition_variable condition_;

    public:
        // Enqueue a message
        void enqueue(const Message& message) {
            unique_lock<mutex> lock(mutex_);
            queue_.push(message);
            lock.unlock();
            condition_.notify_one();
        }

        // Dequeue a message
        Message dequeue() {
            unique_lock<mutex> lock(mutex_);
            // Wait until a message is available
            condition_.wait(lock, [this] { return !queue_.empty(); });

            Message message = queue_.front();
            queue_.pop();
            return message;
        }
};



// Producer function
void producer(MessageQueue& messageQueue, int messageType, const string& payload) {
	Message message;
	message.messageType = messageType;
	message.payload = payload;

	messageQueue.enqueue(message);
}

// Consumer function
void consumer(MessageQueue& messageQueue) {
	while (true) {
		Message message = messageQueue.dequeue();
        int messageType = message.messageType;
        string payload = message.payload;

        // if(messageType == 1){
        //     cout<<payload<<"\n";
        // }
        if(messageType == 1){
            int time = rand()%10;
            thread::id id = this_thread::get_id();
            cout<<id<<" sleeping for "<<time<<"secs \n";

            this_thread::sleep_for(chrono::seconds(time));
            string output_message = "message: " + payload + "\nThread: ";
            cout<<output_message<<id<<"\n\n";
        }
	}
}

int main() {
    thread::id id = this_thread::get_id();
    cout<<"main thead: "<<id<<"\n\n";

    MessageQueue messageQueue;
 
    // Create producer and consumer threads
    thread producerThread1(producer, ref(messageQueue), 1, "Hello, World! 1");
    thread producerThread2(producer, ref(messageQueue), 1, "Hello, World! 2");
    thread producerThread3(producer, ref(messageQueue), 1, "Hello, World! 3");
    thread consumerThread1(consumer, ref(messageQueue));
    thread consumerThread2(consumer, ref(messageQueue));
 
    // Wait for threads to finish
    producerThread1.join();
    producerThread2.join();
    producerThread3.join();
    // consumerThread1.join();
    // consumerThread2.join();

    while(true){
        cout<<"Write message here: ";
        string s;
        cin>>s;
        thread producerThread(producer, ref(messageQueue), 1, s);
        producerThread.join();
    }
 
    return 0;
}