import { useEffect, useState } from "react";
import API from "./api";
import "./App.css";


function App() {

  const [tasks, setTasks] = useState([]);
  const [events, setEvents] = useState([]);

  const [newTask, setNewTask] = useState({
    student_id: 4,
    title: "",
    priority: "Medium",
    status: "Pending",
    due_date: ""
  });

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");



  useEffect(() => {

    fetchData();

  }, []);



  const fetchData = async () => {

    try {

      const taskResponse = await API.get("/tasks/");
      const eventResponse = await API.get("/events/");


      setTasks(taskResponse.data.data || []);
      setEvents(eventResponse.data.data || []);


    } catch (err) {

      console.error(err);

      setError(
        "Failed to load planner data."
      );


    } finally {

      setLoading(false);

    }

  };




  const addTask = async (e) => {

    e.preventDefault();


    try {


      await API.post("/tasks/", newTask);


      alert("Task added successfully");


      fetchData();


      setNewTask({

        student_id: 4,
        title: "",
        priority: "Medium",
        status: "Pending",
        due_date: ""

      });



    } catch(error) {

      console.error(error);

      alert("Failed to add task");

    }

  };




  return (

    <div className="container">


      <header className="header">

        <h1>
          Student Academic Planner
        </h1>

        <p>
          Student Management System
        </p>

      </header>



      {
        loading && (

          <div className="message">
            Loading planner data...
          </div>

        )
      }



      {
        error && (

          <div className="error">
            {error}
          </div>

        )
      }





      {/* ADD TASK FORM */}

      <section className="form-section">


        <h2>
          Add New Task
        </h2>


        <form onSubmit={addTask}>


          <input
            type="text"
            placeholder="Task title"
            value={newTask.title}
            required
            onChange={(e)=>
              setNewTask({
                ...newTask,
                title:e.target.value
              })
            }
          />



          <select

            value={newTask.priority}

            onChange={(e)=>
              setNewTask({
                ...newTask,
                priority:e.target.value
              })
            }

          >

            <option>
              High
            </option>

            <option>
              Medium
            </option>

            <option>
              Low
            </option>


          </select>




          <input

            type="date"

            value={newTask.due_date}

            required

            onChange={(e)=>
              setNewTask({
                ...newTask,
                due_date:e.target.value
              })
            }

          />



          <button>
            Add Task
          </button>


        </form>


      </section>






      {/* TASK LIST */}

      <section>


        <h2>
          Tasks
        </h2>


        {
          tasks.map(task => (

            <div
              className="card"
              key={task.task_id}
            >

              <h3>
                {task.title}
              </h3>


              <p>
                Priority: {task.priority}
              </p>


              <p>
                Status: {task.status}
              </p>


              <p>
                Due Date: {task.due_date}
              </p>


              <p>
                Student: {task.student?.full_name}
              </p>


            </div>


          ))
        }


      </section>






      {/* EVENTS */}


      <section>


        <h2>
          Events
        </h2>


        {
          events.map(event => (

            <div
              className="card"
              key={event.event_id}
            >

              <h3>
                {event.title || "Untitled Event"}
              </h3>


              <p>
                Type: {event.event_type}
              </p>


              <p>
                Date: {event.event_date}
              </p>


              <p>
                Location: {event.location}
              </p>


            </div>

          ))
        }


      </section>



    </div>

  );

}


export default App;