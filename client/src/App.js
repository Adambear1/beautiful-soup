import { useEffect, useState } from "react";
// Components
import SearchBar from "./components/SearchBar";
import Card from "./components/Card";
// utils
import database from "./database";
import { apis, utils, StyledCardGrid, StyledSavedGrid } from "./utils";
import { TransitionGroup, CSSTransition } from "react-transition-group";

function App() {
  const [selectedArticles, setSelectedArticles] = useState([]);
  const [displayArticles, setDisplayArticles] = useState([]);
  const [savedArticles, setSavedArticles] = useState([])
  const { articles } = database;
  useEffect(() => {
    setDisplayArticles([]);
    if (selectedArticles.indexOf("NYT") !== -1) {
      apis.searchArticles("NYT").then(({ data }) => {
        data["journal"] = "NYT";
        setDisplayArticles([...displayArticles, ...data]);
      });
    }
    if (selectedArticles.indexOf("WSJ") !== -1) {
      apis.searchArticles("WSJ").then(({ data }) => {
        data["journal"] = "WSJ";
        setDisplayArticles([...displayArticles, ...data]);
      });
    }
  }, [selectedArticles]);

  const saveArticle = (data) => {
    setDisplayArticles(
      [...displayArticles].filter(({ link }) => {
        return link !== data.link;
      })
    );
    apis.saveArticles(data).then(({ data }) => {
      setSavedArticles([...data])
    });
  };

  return (
    <>
      <SearchBar
        articles={articles}
        selectedArticles={selectedArticles}
        setSelectedArticles={setSelectedArticles}
      />
      <div className="container">
        {/* Saved */}
        <TransitionGroup component={StyledSavedGrid}>
          {savedArticles.length > 0 ?
            savedArticles.map(
              ({ journal, link, title, article, date, saved }, index) => (
                <CSSTransition
                  key={index}
                  timeout={300}
                  classNames="transition"
                >
                  <Card
                    journal={journal}
                    link={link}
                    title={title}
                    article={article}
                    saved={saved ? true : false}
                    saveArticle={saveArticle}
                    date={date}
                  />
                </CSSTransition>
              )
            )
          :
          <CSSTransition
          timeout={300}
          classNames="transition">
          <h1 style={{display: "flex"}}>No Saved Cards</h1>
          </CSSTransition>
          }
        </TransitionGroup>
        {/* Regular */}
        <TransitionGroup component={StyledCardGrid}>
          {displayArticles &&
            displayArticles.map(
              ({ journal, link, title, article, date, saved }, index) => (
                <CSSTransition
                  key={index}
                  timeout={300}
                  classNames="transition"
                >
                  <Card
                    journal={journal}
                    link={link}
                    title={title}
                    article={article}
                    saved={saved ? true : false}
                    saveArticle={saveArticle}
                    date={date}
                  />
                </CSSTransition>
              )
            )}
        </TransitionGroup>
      </div>
    </>
  );
}

export default App;
