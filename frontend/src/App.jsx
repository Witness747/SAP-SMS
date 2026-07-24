import { useEffect, useState } from "react";
import API from "./api";
import "./App.css";


function App() {

  const [tasks, setTasks] = useState([]);
  const [events, setEvents] = useState([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");


  useEffect(() => {

    const fetchData = async () => {

      try {

        const taskResponse = await API.get("/tasks/");
        const eventResponse = await API.get("/events/");


        console.log("TASK RESPONSE:", taskResponse.data);
        console.log("EVENT RESPONSE:", eventResponse.data);


        // FastAPI PaginationResponse format
        setTasks(taskResponse.data.data || []);

        setEvents(eventResponse.data.data || []);


      } catch (err) {

        console.error(err);

        setError(
          "Failed to load planner data. Check backend connection."
        );

      } finally {

        setLoading(false);

      }

    };


    fetchData();

  }, []);



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



      {loading && (
        <div className="message">
          Loading planner data...
        </div>
      )}



      {error && (
        <div className="error">
          {error}
        </div>
      )}



      <section>

        <h2>
          Tasks
        </h2>


        {
          tasks.length === 0 && !loading && (
            <p className="empty">
              No tasks available
            </p>
          )
        }



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
                <strong>
                  Priority:
                </strong>{" "}
                {task.priority}
              </p>


              <p>
                <strong>
                  Status:
                </strong>{" "}
                {task.status}
              </p>


              <p>
                <strong>
                  Due Date:
                </strong>{" "}
                {task.due_date}
              </p>


              <p>
                <strong>
                  Student:
                </strong>{" "}
                {task.student?.full_name}
              </p>


            </div>

          ))
        }


      </section>






      <section>

        <h2>
          Events
        </h2>



        {
          events.length === 0 && !loading && (
            <p className="empty">
              No events available
            </p>
          )
        }




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
                <strong>
                  Type:
                </strong>{" "}
                {event.event_type}
              </p>


              <p>
                <strong>
                  Date:
                </strong>{" "}
                {event.event_date}
              </p>


              <p>
                <strong>
                  Time:
                </strong>{" "}
                {event.start_time} - {event.end_time}
              </p>


              <p>
                <strong>
                  Location:
                </strong>{" "}
                {event.location}
              </p>


              <p>
                <strong>
                  Student:
                </strong>{" "}
                {event.student?.full_name}
              </p>


            </div>


          ))
        }


      </section>


    </div>

  );

}


export default App;