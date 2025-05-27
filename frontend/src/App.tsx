import { useState, useEffect } from 'react'
import './App.css'
import { Box, Typography, Grid, Button, Divider, TextField, Stack } from '@mui/material'
import type { Book, NewBook } from './types'
import BookComponent from './Book'

function App() {

  const [books, setBooks] = useState<Book[]>([])
  const [bookToAdd, setBookToAdd] = useState<NewBook>({
    title: '',
    author: '',
    dateRead: '',
    dateAdded: '',
  })

  const [addingBook, setAddingBook] = useState<boolean>(false)

  useEffect(() => {
    const fetchBooks = async () => {
      const response = await fetch('http://localhost:8000/books', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
      const data = await response.json()
      setBooks(data)
      console.log(data)
    }
    fetchBooks()
  }, [])

  const handleNewBookChange = (field: keyof NewBook, value: string) => {
    setBookToAdd((prev) => ({
      ...prev,
      [field]: value,
    }))
    console.log(bookToAdd)
  }

  const handleBookAddCancel = () =>{
    setAddingBook(false)
    setBookToAdd({
      title: '',
      author: '',
      dateRead: '',
      dateAdded: '',
    })
  }

  const handleNewBookSubmit = () => {
    console.log(bookToAdd)
  }

  return (
    <Box>
      <Typography variant="h4" align="center">
        Welcome to your Reading List!
      </Typography>
      <Typography variant="h5" align="center">
        This is a simple app to keep track of your reading list.
      </Typography>
      <Box>
        {books.length > 0 ? (
          <Grid container spacing={2} justifyContent="center">
            {books.map((book) => (
              <BookComponent key={book.id} book={book} />
            ))}
          </Grid>
        ) : (
          <Typography variant="h6" align="center">
            No books found. Please add some books to your reading list.
          </Typography>
        )}
        <Button variant="contained" color="primary" onClick={() => setAddingBook(true)}>
          Add Book
        </Button>
        {addingBook && (
          <>
            <Divider sx={{ backgroundColor: 'white' }} />
            <Box component='form' noValidate autoComplete='off'>
              <TextField
                sx = {{color: 'white'}}
                label="Title"
                variant="outlined"
                fullWidth
                margin="normal"
                onChange={(e) => handleNewBookChange('title', e.target.value)}
                value={bookToAdd.title}
              />
              <TextField
                label="Author"
                variant="outlined"
                fullWidth
                margin="normal"
                onChange={(e) => handleNewBookChange('author', e.target.value)}
                value={bookToAdd.author}
              />
              <TextField
                label="Date Read"
                variant="outlined"
                fullWidth
                margin="normal"
                onChange={(e) => handleNewBookChange('dateRead', e.target.value)}
                value={bookToAdd.dateRead}
              />
              <TextField
                label="Date Added"
                variant="outlined"
                fullWidth
                margin="normal"
                onChange={(e) => handleNewBookChange('dateAdded', e.target.value)}
                value={bookToAdd.dateAdded}
              />
            </Box>
            <Stack spacing={2} direction="row" justifyContent="center">
            <Button variant="contained" color="secondary" onClick={() => handleBookAddCancel()}>
              Cancel
            </Button>
            <Button variant="contained" color="primary" onClick={handleNewBookSubmit}>
              Submit New Book
            </Button>
            </Stack>
          </>
        )}
      </Box>
    </Box>
  )
}

export default App
